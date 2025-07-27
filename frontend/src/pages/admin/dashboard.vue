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
            class="text-md mb-4 rounded-lg bg-blue-50 p-1 text-center font-semibold text-theme-300"
          >
            Category Type
          </h2>
          <div class="flex flex-col items-center justify-center">
            <canvas ref="expenseDonutChart" width="450" height="300"></canvas>
          </div>
        </div>
        <div class="rounded-lg bg-white p-6 shadow-xl">
          <h2
            class="text-md mb-4 rounded-lg bg-blue-50 p-1 text-center font-semibold text-theme-300"
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
            class="text-md mb-4 rounded-lg bg-blue-50 p-1 text-center font-semibold text-theme-300"
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

  // Register Chart.js plugins globally
  Chart.register(ChartDataLabels);

  // --- Reactive State ---
  const adminClaimStore = useAdminClaimStore();
  const loading = ref(true);
  const error = ref("");

  // --- Template Refs for Canvas Elements ---
  const expenseDonutChart = ref(null);
  const categoryBarChart = ref(null);
  const expenseLineChart = ref(null);

  // --- Chart.js Instance Variables (to manage chart lifecycle) ---
  let expenseDonutChartInstance = null;
  let categoryBarChartInstance = null;
  let expenseLineChartInstance = null;

  // --- Chart.js Plugin: Custom Center Text for Donut Chart ---
  // This plugin draws "Total Expenses" and the calculated sum in the center of the donut chart.
  Chart.register({
    id: "centerText",
    afterDraw(chart) {
      if (chart.config.type !== "doughnut") return; // Apply only to doughnut charts

      const {
        ctx,
        chartArea: { width, height },
      } = chart;
      ctx.save(); // Save the current canvas state

      // First line of text: "Total Expenses:"
      ctx.font = "12px Inter";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText("Total Expenses:", width / 2, height / 2 - 10);

      // Calculate the total amount from all claims for the second line
      const totalAmountAllClaims = adminClaimStore.claims.reduce(
        (claimSum, claim) => {
          // Sum invoices within each claim
          const claimInvoicesTotal =
            claim.invoices?.reduce((invoiceSum, invoice) => {
              // Sum items/services within each invoice
              const invoiceItemsTotal =
                invoice.itemsServices?.reduce(
                  (currentSum, item) =>
                    currentSum + item.quantity * item.unit_price,
                  0,
                ) || 0;
              return invoiceSum + invoiceItemsTotal;
            }, 0) || 0;
          return claimSum + claimInvoicesTotal;
        },
        0,
      );

      // Second line of text: the total calculated amount
      ctx.font = "bold 13px Inter";
      ctx.fillText(
        "RM " +
          totalAmountAllClaims.toLocaleString("en-MY", {
            minimumFractionDigits: 2,
          }),
        width / 2,
        height / 2 + 8,
      );
      ctx.restore(); // Restore the canvas state
    },
  });

  // --- Static Budget Data ---
  // Budgets for the Horizontal Bar Chart (Category-wise)
  const categoryBudgets = {
    "Medical \nExpenses": 100000,
    Accommodation: 100000,
    "Meals &\nEntertainment": 100000,
    "Supplies &\nEquipment": 100000,
    "Travel \nExpenses": 100000,
  };

  // Budgets for the Line Chart (Yearly)
  const yearlyBudgets = {
    2023: 500000,
    2024: 550000,
    2025: 400000,
  };

  // --- Function to Process Data and Render/Update Charts ---
  const processAndRenderCharts = () => {
    const claimsData = adminClaimStore.claims;

    // 1. Destroy any existing chart instances to prevent memory leaks and ensure clean re-rendering
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

    // Early exit if no claims data or if canvas elements are not yet available
    if (!claimsData || claimsData.length === 0) {
      console.log("No claims data available, charts not rendered.");
      return;
    }
    if (
      !expenseDonutChart.value ||
      !categoryBarChart.value ||
      !expenseLineChart.value
    ) {
      console.warn(
        "Chart canvas refs are not yet available. Skipping chart rendering.",
      );
      return;
    }

    // --- 2. Data Processing for Donut Chart (Category Type) ---
    const categoryAmountTotals = {};
    claimsData.forEach((claim) => {
      claim.invoices.forEach((invoice) => {
        // Normalize category names to match the keys defined in `categoryBudgets`
        let normalizedCategory = invoice.category || "Uncategorized";
        if (normalizedCategory === "Medical Expenses") {
          normalizedCategory = "Medical \nExpenses";
        } else if (normalizedCategory === "Meals & Entertaiment") {
          normalizedCategory = "Meals &\nEntertainment";
        } else if (normalizedCategory === "Supplies and Equipment") {
          normalizedCategory = "Supplies &\nEquipment";
        } else if (normalizedCategory === "Travel Expenses") {
          normalizedCategory = "Travel \nExpenses";
        }

        // Aggregate total amount for each normalized category
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

    const donutChartLabels = Object.keys(categoryAmountTotals);
    const donutChartPercentData = donutChartLabels.map((cat) =>
      ((categoryAmountTotals[cat] / totalAmountAll) * 100).toFixed(2),
    );

    // --- 3. Data Processing for Bar Chart (Total Expenses vs Total Budget) ---
    const barChartDataKeys = Object.keys(categoryBudgets);
    // Prepare labels for multiline display on the Y-axis
    const barChartLabels = barChartDataKeys.map((key) => key.split("\n"));

    // Get claimed amounts (expenses) for each category
    const barChartClaimedAmounts = barChartDataKeys.map(
      (cat) => categoryAmountTotals[cat] || 0, // Using actual unscaled amounts
    );
    // Get budget amounts for each category
    const barChartBudgetAmounts = barChartDataKeys.map(
      (cat) => categoryBudgets[cat],
    ); // Using actual unscaled amounts

    // --- 4. Data Processing for Line Chart (Total Expenses Over Years) ---
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

    const lineChartYearLabels = Object.keys(yearlyBudgets).sort(); // Ensure years are sorted
    const lineChartYearData = lineChartYearLabels.map(
      (y) => yearAmounts[y] || 0,
    );
    const lineChartYearBudgetData = lineChartYearLabels.map(
      (y) => yearlyBudgets[y] || 0,
    );

    // --- 5. Chart Rendering ---

    // Donut Chart Initialization
    expenseDonutChartInstance = new Chart(expenseDonutChart.value, {
      type: "doughnut",
      data: {
        labels: donutChartLabels,
        datasets: [
          {
            data: donutChartPercentData,
            backgroundColor: [
              "#FFAD05",
              "#2A9D8F",
              "#00246A",
              "#0353A4",
              "#CAE9FF",
            ],
          },
        ],
      },
      options: {
        cutout: "65%", // Defines the size of the center hole
        responsive: false, // Disables Chart.js's built-in responsiveness
        plugins: {
          legend: {
            position: "right", // Position legend to the right
            labels: {
              boxWidth: 14,
              boxHeight: 14,
              font: { size: 12 },
              padding: 10,
            },
          },
          datalabels: { display: false }, // Hide default datalabels (custom plugin handles center text)
          tooltip: {
            callbacks: {
              label: (context) => `  ${context.raw || 0}%`, // Custom tooltip format for percentages
            },
          },
        },
      },
      plugins: ["centerText"], // Enable the custom centerText plugin
    });

    // Horizontal Bar Chart Initialization
    categoryBarChartInstance = new Chart(categoryBarChart.value, {
      type: "bar",
      data: {
        labels: barChartLabels,
        datasets: [
          {
            label: "Total Expenses",
            data: barChartClaimedAmounts, // Actual unscaled expense amounts
            backgroundColor: "#0353A4",
            borderRadius: 6,
            barPercentage: 0.9,
            categoryPercentage: 0.8,
            datalabels: {
              anchor: "end",
              align: "end",
              color: "#222",
              font: { family: "Inter, sans-serif", weight: "bold", size: 12 },
              formatter: (v) =>
                `RM ${Number(v).toLocaleString("en-MY", { minimumFractionDigits: 0 })}`, // Format as currency
              clamp: true, // Keep labels within the chart area
            },
            tooltip: {
              callbacks: {
                label: (context) => {
                  const originalCategoryKey =
                    barChartDataKeys[context.dataIndex];
                  const value = context.raw; // The actual expense value
                  const budget = categoryBudgets[originalCategoryKey] || 0; // The actual budget value

                  let percent = budget
                    ? ((value / budget) * 100).toFixed(2)
                    : "N/A";

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
            data: barChartBudgetAmounts, // Actual unscaled budget amounts
            backgroundColor: "#FFAD05",
            borderRadius: 6,
            barPercentage: 0.9,
            categoryPercentage: 0.8,
            datalabels: {
              anchor: "end",
              align: "end",
              color: "#222",
              font: {
                family: "Inter, sans-serif",
                weight: "regular",
                size: 11,
              },
              formatter: (v) => {
                return `RM ${Number(v).toLocaleString("en-MY", { minimumFractionDigits: 0 })}`; // Format as currency
              },
              clamp: true,
            },
          },
        ],
      },
      options: {
        indexAxis: "y", // Make bars horizontal
        responsive: false,
        maintainAspectRatio: false, // Allow custom width/height
        layout: {
          padding: {
            left: 0,
            right: 60, // Add padding on the right for datalabels
            top: 5,
          },
        },
        plugins: {
          legend: {
            position: "top",
            labels: { boxWidth: 14, boxHeight: 14, font: { size: 12 } },
          },
          datalabels: { display: true }, // Enable datalabels for this chart
        },
        scales: {
          x: {
            beginAtZero: true,
            display: false, // Hide the numerical X-axis
            max:
              Math.max(...barChartClaimedAmounts, ...barChartBudgetAmounts) *
                1.1 || 100000, // Dynamic max based on largest value + buffer
            title: { display: false },
            grid: { display: false },
            ticks: { font: { family: "Inter, sans-serif", size: 11 } },
          },
          y: {
            title: { display: false, text: "Category" },
            grid: { display: false },
            ticks: {
              font: { family: "Inter, sans-serif", size: 12 },
              callback: function (value) {
                return this.getLabelForValue(value); // Display original category label (handles newlines)
              },
            },
          },
        },
      },
      plugins: [ChartDataLabels], // Ensure datalabels plugin is applied to this chart
    });

    // Line Chart Initialization
    const ctx = expenseLineChart.value.getContext("2d");
    // Create gradient for expense area fill
    const expenseGradient = ctx.createLinearGradient(0, 0, 0, 300);
    expenseGradient.addColorStop(0, "rgba(3,83,164,1)"); // Solid blue at top
    expenseGradient.addColorStop(1, "rgba(3,83,164,0.15)"); // Fading blue at bottom

    // Create gradient for budget area fill (though fill is false, good practice)
    const budgetGradient = ctx.createLinearGradient(0, 0, 0, 300);
    budgetGradient.addColorStop(0, "rgba(251,191,36,1)"); // Solid yellow at top
    budgetGradient.addColorStop(1, "rgba(251,191,36,0.15)"); // Fading yellow at bottom

    expenseLineChartInstance = new Chart(expenseLineChart.value, {
      type: "line",
      data: {
        labels: lineChartYearLabels,
        datasets: [
          {
            label: "Total Expenses",
            data: lineChartYearData,
            fill: true, // Fill the area under the line
            borderColor: "#0353A4",
            backgroundColor: expenseGradient,
            tension: 0.1, // Smooth the line
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
                  const expense = lineChartYearData[yearIndex];
                  const budget = lineChartYearBudgetData[yearIndex];
                  let percent = budget
                    ? ((expense / budget) * 100).toFixed(2)
                    : "N/A";
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
            data: lineChartYearBudgetData,
            fill: false, // Only show the line, no fill
            borderColor: "#FFAD05",
            backgroundColor: budgetGradient, // Though fill is false, keeping for consistency
            borderDash: [3, 3], // Dashed line style
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
          padding: { left: 40, right: 40 }, // Padding around the chart area
        },
        plugins: {
          legend: {
            position: "top",
            labels: {
              boxWidth: 14,
              boxHeight: 14,
              font: { family: "Inter, sans-serif", size: 12 },
            },
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            display: false, // Hide Y-axis numerical labels
            max:
              Math.max(...lineChartYearData, ...lineChartYearBudgetData) *
                1.1 || 10000, // Dynamic max with buffer
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

  // --- Lifecycle Hooks and Watchers ---

  // Watch for changes in the adminClaimStore.claims array
  // Deep watch ensures reactivity to changes within objects inside the array.
  watch(
    () => adminClaimStore.claims,
    () => {
      // Use nextTick to ensure DOM is updated before attempting to re-render charts
      nextTick(() => {
        processAndRenderCharts();
      });
    },
    { deep: true },
  );

  // On component mount: fetch data and render charts
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
      // Ensure DOM is updated after loading data, then render charts
      await nextTick();
      processAndRenderCharts();
    }
  });

  // On component unmount: destroy chart instances to prevent memory leaks
  onUnmounted(() => {
    if (expenseDonutChartInstance) expenseDonutChartInstance.destroy();
    if (categoryBarChartInstance) categoryBarChartInstance.destroy();
    if (expenseLineChartInstance) expenseLineChartInstance.destroy();
  });
</script>
