<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <div v-if="loading" class="text-center text-lg font-semibold text-gray-700">
      Loading dashboard data...
    </div>
    <div v-if="error" class="text-center text-lg font-semibold text-red-500">
      Error: {{ error }}
    </div>

    <template v-if="!loading && !error">
      <AdminClaimsCard
        :totalCount="adminClaimStore.totalClaimCount"
        :approvedCount="adminClaimStore.approvedClaimsCount"
        :rejectedCount="adminClaimStore.rejectedClaimsCount"
      />
      <div class="grid grid-cols-2 gap-6 px-4 sm:px-8 lg:px-14">
        <div class="rounded-lg bg-white p-6 shadow-xl">
          <h2
            class="mb-4 rounded-lg bg-blue-50 p-1 text-center text-md font-semibold text-theme-300"
          >
            Category Type
          </h2>
          <div class="flex flex-col items-center justify-center">
            <canvas ref="expenseDonutChart" width="450" height="300"></canvas>
          </div>
        </div>
        <div class="rounded-lg bg-white p-6 shadow-xl">
          <h2
            class="mb-4 rounded-lg bg-blue-50 p-1 text-center text-md font-semibold text-theme-300"
          >
            Total Expenses vs Total Budget
          </h2>
          <div class="flex flex-col items-center justify-center">
            <canvas ref="categoryBarChart" width="450" height="300"></canvas>
          </div>
        </div>
      </div>
      <div class="mt-8 grid gap-6 px-4 sm:px-8 lg:px-14">
        <div class="rounded-lg bg-white p-6 shadow-xl">
          <h2
            class="mb-4 rounded-lg bg-blue-50 p-1 text-center text-md font-semibold text-theme-300"
          >
            Total Expenses Over Years
          </h2>
          <canvas ref="expenseLineChart" width="350" height="150"></canvas>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { onMounted, ref, watch, nextTick, onUnmounted } from "vue";
import Chart from "chart.js/auto";
import ChartDataLabels from "chartjs-plugin-datalabels";
import { useAdminClaimStore } from "@/stores/admin-claims.ts";
Chart.register(ChartDataLabels);

const adminClaimStore = useAdminClaimStore();
const loading = ref(true);
const error = ref("");

// Refs for canvas elements
const expenseDonutChart = ref(null);
const categoryBarChart = ref(null);
const expenseLineChart = ref(null);

// Variables to hold Chart.js instances
let expenseDonutChartInstance = null;
let categoryBarChartInstance = null;
let expenseLineChartInstance = null;

// Chart.js plugin for center text in donut
Chart.register({
  id: "centerText",
  afterDraw(chart) {
    if (chart.config.type !== "doughnut") return;
    const {
      ctx,
      chartArea: { width, height },
    } = chart;
    ctx.save();
    ctx.font = " 10px Inter";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("Total Expenses:", width / 2, height / 2 - 10);
    // Second line: total amount
    const totalAmountAllClaims = adminClaimStore.claims.reduce((claimSum, claim) => {
      return (
        claimSum +
        (claim.invoices?.reduce((invoiceSum, invoice) => {
          return (
            invoiceSum +
            (invoice.itemsServices?.reduce(
              (currentSum, item) => currentSum + item.quantity * item.unit_price,
              0,
            ) || 0)
          );
        }, 0) || 0)
      );
    }, 0);
    ctx.font = "bold 13px Inter";
    ctx.fillText(
      "RM " +
        totalAmountAllClaims.toLocaleString("en-MY", {
          minimumFractionDigits: 2,
        }),
      width / 2,
      height / 2 + 8,
    );
    ctx.restore();
  },
});

// Horizontal Bar Chart Data (Claims by Category)
const categoryBudgets = {
  "Medical \nExpenses": 100000,
  "Accommodation": 100000,
  "Meals &\nEntertainment": 100000, // Corrected typo here from Entertaiment
  "Supplies &\nEquipment": 100000,
  "Travel \nExpenses": 100000,
};

// Line Chart (Expenses over Years)
const yearlyBudgets = {
  2023: 500000,
  2024: 550000,
  2025: 400000,
};

// Function to process data and render/update charts
const processAndRenderCharts = () => {
  const claimsData = adminClaimStore.claims;

  // Destroy existing charts and nullify instances
  if (expenseDonutChartInstance) {
    expenseDonutChartInstance.destroy();
    expenseDonutChartInstance = null;
  }
  if (categoryBarChartInstance) {
    categoryBarChartInstance.destroy();
    categoryBarChartInstance = null;
  }
  if (expenseLineChartInstance) {
    expenseLineChartInstance.destroy();
    expenseLineChartInstance = null;
  }

  // If no claims data, just return after destroying existing charts
  if (!claimsData || claimsData.length === 0) {
    console.log("No claims data available, charts not rendered.");
    return;
  }

  // Ensure canvas elements are available before rendering
  if (!expenseDonutChart.value || !categoryBarChart.value || !expenseLineChart.value) {
    console.warn("Chart canvas refs are not yet available. Skipping chart rendering.");
    return;
  }

  // --- Data Processing for Donut Chart (Category Type) ---
  const categoryAmountTotals = {};
  claimsData.forEach((claim) => {
    claim.invoices.forEach((invoice) => {
      // Normalizing category names to match budget keys
      let normalizedCategory = invoice.category || "Uncategorized";
       if (normalizedCategory === "Medical Expenses") {
        normalizedCategory = "Medical \nExpenses";
      } else if (normalizedCategory === "Meals & Entertaiment") { // Fix typo and add newline
         normalizedCategory = "Meals &\nEntertainment";
      } else if (normalizedCategory === "Supplies and Equipment") {
        normalizedCategory = "Supplies &\nEquipment";
      } else if (normalizedCategory === "Travel Expenses") {
        normalizedCategory = "Travel \nExpenses";
      }

      categoryAmountTotals[normalizedCategory] =
        (categoryAmountTotals[normalizedCategory] || 0) +
        (invoice.itemsServices?.reduce(
          (itemSum, item) => itemSum + item.quantity * item.unit_price,
          0,
        ) || 0);
    });
  });

  const totalAmountAll = Object.values(categoryAmountTotals).reduce(
    (sum, val) => sum + val,
    0,
  );

  const categoryLabels = Object.keys(categoryAmountTotals);
  const categoryPercentData = categoryLabels.map((cat) =>
    ((categoryAmountTotals[cat] / totalAmountAll) * 100).toFixed(2),
  );

  // --- Data Processing for Bar Chart (Total Expenses vs Total Budget) ---
  const barDataKeys = Object.keys(categoryBudgets);
  const chartBarLabels = barDataKeys.map(key => key.split('\n'));
  const claimedAmounts = barDataKeys.map(
    (cat) => (categoryAmountTotals[cat] || 0) / 5000, // Data scaled down by 5000
  );
  const budgetAmounts = barDataKeys.map((cat) => categoryBudgets[cat] / 5000); // Data scaled down by 5000

  // --- Data Processing for Line Chart (Total Expenses Over Years) ---
  const yearAmounts = {};
  claimsData.forEach((claim) => {
    const year = new Date(claim.submitted_date).getFullYear();
    const claimTotalFromInvoices =
      claim.invoices?.reduce((invoiceSum, invoice) => {
        return (
          invoiceSum +
          (invoice.itemsServices?.reduce(
            (itemSum, item) => itemSum + item.quantity * item.unit_price,
            0,
          ) || 0)
        );
      }, 0) || 0;
    yearAmounts[year] = (yearAmounts[year] || 0) + claimTotalFromInvoices;
  });
  const yearLabels = Object.keys(yearlyBudgets).sort();
  const yearData = yearLabels.map((y) => yearAmounts[y] || 0);
  const yearBudgetData = yearLabels.map((y) => yearlyBudgets[y] || 0);

  // --- Chart Rendering ---

  // Donut Chart
  expenseDonutChartInstance = new Chart(expenseDonutChart.value, {
    type: "doughnut",
    data: {
      labels: categoryLabels,
      datasets: [
        {
          data: categoryPercentData,
          backgroundColor: ["#FFAD05", "#2A9D8F", "#00246A", "#0353A4", "#CAE9FF"],
        },
      ],
    },
    options: {
      cutout: "65%",
      responsive: false,
      plugins: {
        legend: {
          position: "right",
          labels: {
            boxWidth: 14,
            boxHeight: 14,
            font: { size: 12 },
            padding: 10,
          },
        },
        datalabels: { display: false },
        tooltip: {
          callbacks: {
            label: (context) => `  ${context.raw || 0}%`,
          },
        },
      },
    },
    plugins: ["centerText"],
  });

  // Horizontal Bar Chart
  categoryBarChartInstance = new Chart(categoryBarChart.value, {
    type: "bar",
    data: {
      labels: chartBarLabels,
      datasets: [
        {
          label: "Total Expenses",
          data: claimedAmounts, // Scaled data
          backgroundColor: "#0353A4",
          borderRadius: 6,
          barPercentage: 0.9,
          categoryPercentage: 0.8,
          datalabels: {
            anchor: "end",
            align: "end",
            color: "#222",
            font: { family: "Inter, sans-serif", weight: "bold", size: 11 },
            formatter: (v) =>
              `RM ${Number(v * 5000).toLocaleString("en-MY", { minimumFractionDigits: 0 })}`, // Display original value
            clamp: true,
          },
          tooltip: {
            callbacks: {
              label: (context) => {
                const category = context.label;
                const value = context.raw * 5000; // Display original value
                const budget = categoryBudgets[category] || 0;
                let percent = budget ? ((value / budget) * 100).toFixed(2) : "N/A";
                return [
                  `Expenses: RM ${Number(value).toLocaleString("en-MY")}`,
                  `Budget: RM ${Number(budget).toLocaleString("en-MY")}`,
                  `Expenses over Budget: ${percent}%`,
                ];
              },
            },
          },
        },
        {
          label: "Total Budget",
          data: budgetAmounts, // Scaled data
          backgroundColor: "#FFAD05",
          borderRadius: 6,
          barPercentage: 0.9,
          categoryPercentage: 0.8,
          datalabels: {
            anchor: "end",
            align: "end",
            color: "#222",
            font: { family: "Inter, sans-serif", weight: "regular", size: 11 },
            formatter: (v) =>
              `RM ${Number(v * 5000).toLocaleString("en-MY", { minimumFractionDigits: 0 })}`, // Display original value
            clamp: true,
          },
        },
      ],
    },
    options: {
      indexAxis: "y",
      responsive: false,
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 0,
          right: 60,
          top: 5
        },
      },
      plugins: {
        legend: {
          position: "top",
          labels: { boxWidth: 14, boxHeight: 14, font: { size: 12 } },
        },
        datalabels: { display: true },
      },
      scales: {
        x: {
          beginAtZero: true,
          display: false, // Hide the numerical X-axis to avoid clutter
          max: (Math.max(...claimedAmounts, ...budgetAmounts) * 1.1) || 10, // Max based on scaled data
          title: { display: false },
          grid: { display: false },
          ticks: { font: { family: "Inter, sans-serif", size: 11 } },
        },
        y: {
          title: { display: false, text: "Category" },
          grid: { display: false },
          ticks: {
            font: { family: "Inter, sans-serif", size: 11 },
            callback: function (value) {
            return this.getLabelForValue(value);
            },
          },
        },
      },
    },
    plugins: [ChartDataLabels],
  });

  // Line Chart
  const ctx = expenseLineChart.value.getContext("2d");
  const expenseGradient = ctx.createLinearGradient(0, 0, 0, 300);
  expenseGradient.addColorStop(0, "rgba(3,83,164,1)");
  expenseGradient.addColorStop(1, "rgba(3,83,164,0.15)");

  const budgetGradient = ctx.createLinearGradient(0, 0, 0, 300);
  budgetGradient.addColorStop(0, "rgba(251,191,36,1)");
  budgetGradient.addColorStop(1, "rgba(251,191,36,0.15)");

  expenseLineChartInstance = new Chart(expenseLineChart.value, {
    type: "line",
    data: {
      labels: yearLabels,
      datasets: [
        {
          label: "Total Expenses",
          data: yearData,
          fill: true,
          borderColor: "#0353A4",
          backgroundColor: expenseGradient,
          tension: 0.1,
          pointBackgroundColor: "#0353A4",
          borderWidth: 2,
          datalabels: {
            anchor: "top",
            align: "end",
            formatter: (v) =>
              `RM ${Number(v).toLocaleString("en-MY", { minimumFractionDigits: 0 })}`,
            clamp: true,
            font: { family: "Inter, sans-serif", weight: "bold", size: 12 },
            color: "#000",
          },
          tooltip: {
            callbacks: {
              label: (context) => {
                const yearIndex = context.dataIndex;
                const expense = yearData[yearIndex];
                const budget = yearBudgetData[yearIndex];
                let percent = budget ? ((expense / budget) * 100).toFixed(2) : "N/A";
                return [
                  `Expense: RM ${Number(expense).toLocaleString("en-MY")}`,
                  `Budget: RM ${Number(budget).toLocaleString("en-MY")}`,
                  `Expense over Budget: ${percent}%`,
                ];
              },
            },
          },
        },
        {
          label: "Total Budget",
          data: yearBudgetData,
          fill: false,
          borderColor: "#FFAD05",
          backgroundColor: budgetGradient,
          borderDash: [3, 3],
          borderWidth: 2,
          tension: 0.1,
          pointBackgroundColor: "#FFAD05",
          datalabels: {
            anchor: "top",
            align: "end",
            formatter: (v) =>
              `RM ${Number(v).toLocaleString("en-MY", { minimumFractionDigits: 0 })}`,
            clamp: true,
            font: { family: "Inter, sans-serif", size: 12 },
            color: "#000",
          },
        },
      ],
    },
    options: {
      responsive: true,
      layout: {
        padding: { left: 40, right: 40 },
      },
      plugins: {
        legend: {
          position: "top",
          labels: { boxWidth: 14, boxHeight: 14, font: { family: "Inter, sans-serif", size: 12 } },
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          display: false,
          max: Math.max(...yearData, ...yearBudgetData) * 1.1 || 10000,
          title: { display: true, text: "Amount (RM)" },
          grid: { display: false },
          ticks: { font: { family: "Inter, sans-serif", size: 12 } },
        },
        x: {
          title: {
            display: true,
            text: "Year",
            font: { family: "Inter, sans-serif", weight: "bold", size: 14 },
            color: "#000",
          },
          grid: { display: true },
          ticks: { font: { family: "Inter, sans-serif", size: 12 } },
        },
      },
    },
  });
};

watch(
  () => adminClaimStore.claims,
  () => {
    nextTick(() => {
      processAndRenderCharts();
    });
  },
  { deep: true },
);

onMounted(async () => {
  loading.value = true;
  error.value = null;
  try {
    await adminClaimStore.fetchAdminClaims();
  } catch (err) {
    console.error("Failed to load dashboard claims:", err);
    error.value = "Failed to load dashboard data. Please try again later.";
  } finally {
    loading.value = false;
    await nextTick();
    processAndRenderCharts();
  }
});

onUnmounted(() => {
  if (expenseDonutChartInstance) expenseDonutChartInstance.destroy();
  if (categoryBarChartInstance) categoryBarChartInstance.destroy();
  if (expenseLineChartInstance) expenseLineChartInstance.destroy();
});
</script>
