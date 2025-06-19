<template>
  <div class="mx-auto my-14 w-full max-w-6xl bg-gray-100">
    <AdminClaimsCard :totalCount="11" :approvedCount="8" :rejectedCount="3" />

    <div class="grid grid-cols-2 gap-6 px-4 sm:px-8 lg:px-14">
      <!-- Category Type Donut Chart -->
      <div class="bg-white rounded-lg shadow-xl p-6">
        <h2 class="text-lg font-semibold text-center mb-4 text-theme-300 bg-blue-50 rounded-lg p-1">Category Type</h2>
        <div class="flex flex-col items-center justify-center">
          <canvas id="expenseDonutChart" width="450" height="250"></canvas>
        </div>
      </div>
      <!-- Horizontal Bar Chart -->
      <div class="bg-white rounded-lg shadow-xl p-6">
        <h2 class="text-lg font-semibold mb-4 text-center text-theme-300 bg-blue-50 rounded-lg p-1">Total Expenses vs
          Total Budget</h2>
        <div class="flex flex-col items-center justify-center">
          <canvas id="categoryBarChart" width="450" height="250"></canvas>
        </div>
      </div>
    </div>
    <div class="grid mt-8 gap-6 px-4 sm:px-8 lg:px-14">
      <!-- Expense Over Years Line Chart -->
      <div class="bg-white rounded-lg shadow-xl p-6">
        <h2 class="text-lg font-semibold mb-4 text-center text-theme-300 bg-blue-50 rounded-lg p-1">Total Expenses Over
          Years</h2>
        <canvas id="expenseLineChart" width="350" height="150"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import Chart from "chart.js/auto";
import ChartDataLabels from "chartjs-plugin-datalabels";
Chart.register(ChartDataLabels);

// Mock data for demonstration
const claims = [
  { id: 1, category: "Supplies &\nEquipment", amount: 1200, date: "2023-06-01", expenseType: "Hardware", status: "approved" },
  { id: 2, category: "Travel", amount: 800, date: "2023-06-02", expenseType: "Transport", status: "approved" },
  { id: 3, category: "Meals &\nEntertainment", amount: 300, date: "2023-06-02", expenseType: "Food", status: "rejected" },
  { id: 4, category: "Supplies &\nEquipment", amount: 2000, date: "2024-06-03", expenseType: "Hardware", status: "approved" },
  { id: 5, category: "Accommodation", amount: 1500, date: "2024-06-04", expenseType: "Lodging", status: "approved" },
  { id: 6, category: "Travel", amount: 600, date: "2024-06-04", expenseType: "Transport", status: "rejected" },
  { id: 7, category: "Supplies &\nEquipment", amount: 900, date: "2025-06-05", expenseType: "Hardware", status: "approved" },
  { id: 8, category: "Meals &\nEntertainment", amount: 400, date: "2025-06-05", expenseType: "Food", status: "approved" },
  { id: 9, category: "Accommodation", amount: 1200, date: "2025-07-01", expenseType: "Lodging", status: "approved" },
  { id: 10, category: "Travel", amount: 700, date: "2025-07-02", expenseType: "Transport", status: "approved" },
  { id: 11, category: "Medical", amount: 700, date: "2025-07-29", expenseType: "Medicine", status: "rejected" },
];

// Summary stats
const totalClaims = claims.length;
const totalApprovedClaims = claims.filter(c => c.status === "approved").length;
const totalRejectedClaims = claims.filter(c => c.status === "rejected").length;
const totalAmount = claims.reduce((sum, c) => sum + c.amount, 0);

// Expense Type Donut Chart Data
const categoryAmountTotals = {};
claims.forEach((c) => {
  categoryAmountTotals[c.category] = (categoryAmountTotals[c.category] || 0) + c.amount;
});
const categoryLabels = Object.keys(categoryAmountTotals);

// Calculate total amount for all categories
const totalAmountAll = Object.values(categoryAmountTotals).reduce((sum, val) => sum + val, 0);

// Compute percentage for each category
const categoryPercentData = categoryLabels.map(
  (cat) => ((categoryAmountTotals[cat] / totalAmountAll) * 100).toFixed(2)
);

// Chart.js plugin for center text in donut
Chart.register({
  id: 'centerText',
  afterDraw(chart) {
    if (chart.config.type !== 'doughnut') return;
    const { ctx, chartArea: { width, height } } = chart;
    ctx.save();
    ctx.font = ' 10px Inter';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('Total Expenses:', width / 2, height / 2 - 10);
    // Second line: total amount
    ctx.font = 'bold 13px Inter';
    ctx.fillText('RM ' + totalAmountAll.toLocaleString('en-MY', { minimumFractionDigits: 2 }), width / 2, height / 2 + 8);
  }
});


// Horizontal Bar Chart Data (Claims by Category)
// Example: Set a budget for each category (replace with your real budget data)
const categoryBudgets = {
  "Supplies &\nEquipment": 3000,
  "Travel": 2500,
  "Meals &\nEntertainment": 1000,
  "Accommodation": 2000,
  "Medical": 1000,
};

// Prepare data for each category
const barCategories = Object.keys(categoryBudgets);
const claimedAmounts = barCategories.map(cat =>
  claims.filter(c => c.category === cat).reduce((sum, c) => sum + c.amount, 0)
);
const budgetAmounts = barCategories.map(cat => categoryBudgets[cat]);

// Line Chart (Expenses over Years)
// Prepare data for Expense and Budget Over Years Line Chart
const yearlyBudgets = {
  2023: 6000,
  2024: 7000,
  2025: 6500,
};

const yearAmounts = {};
const yearBudgets = {};
claims.forEach((c) => {
  const year = new Date(c.date).getFullYear();
  yearAmounts[year] = (yearAmounts[year] || 0) + c.amount;
  // // If you want the same budget for each year, sum all categoryBudgets
  // yearBudgets[year] = Object.values(categoryBudgets).reduce((sum, b) => sum + b, 0);
  // Use the yearlyBudgets object for each year
  yearBudgets[year] = yearlyBudgets[year] || 0;
});
const yearLabels = Object.keys(yearAmounts).sort();
const yearData = yearLabels.map((y) => yearAmounts[y]);
const yearBudgetData = yearLabels.map((y) => yearBudgets[y]);

// Chart Styling
onMounted(() => {
  // Expense Type Donut Chart
  new Chart(document.getElementById("expenseDonutChart"), {
    type: "doughnut",
    data: {
      labels: categoryLabels,
      datasets: [
        {
          data: categoryPercentData,
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
            label: function (context) {
              const value = context.raw || 0;
              return `  ${value}%`;
            }
          }
        }
      },
    },
    plugins: ['centerText'],
  });

  // Stacked Horizontal Bar Chart: Total Amount vs Budget
  new Chart(document.getElementById("categoryBarChart"), {
    type: "bar",
    data: {
      labels: barCategories,
      datasets: [
        {
          label: "Total Expenses",
          data: claimedAmounts,
          backgroundColor: "#0353A4",
          borderRadius: 6,
          barPercentage: 0.9,
          categoryPercentage: 0.8,
          datalabels: {
            anchor: 'end',
            align: 'end',
            color: '#222',
            font: {
              family: 'Inter, sans-serif',
              weight: 'bold',
              size: 11
            },
            formatter: v => `RM ${Number(v).toLocaleString('en-MY', { minimumFractionDigits: 0 })}`,
            clamp: true,
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                const category = context.label;
                const value = context.raw;
                const budget = categoryBudgets[category] || 0;
                let percent = budget ? ((value / budget) * 100).toFixed(2) : "N/A";
                return [
                  `Expenses: RM ${Number(value).toLocaleString('en-MY')}`,
                  `Budget: RM ${Number(budget).toLocaleString('en-MY')}`,
                  `Expenses over Budget: ${percent}%`
                ];
              }
            }
          }
        },
        {
          label: "Total Budget",
          data: budgetAmounts,
          backgroundColor: "#FFAD05",
          borderRadius: 6,
          barPercentage: 0.9,
          categoryPercentage: 0.8,
          datalabels: {
            anchor: 'end',
            align: 'end',
            color: '#222',
            font: {
              family: 'Inter, sans-serif',
              weight: 'regular',
              size: 11
            },
            formatter: v => `RM ${Number(v).toLocaleString('en-MY', { minimumFractionDigits: 0 })}`,
            clamp: true,
          }
        },
      ],
    },
    options: {
      indexAxis: "y",
      responsive: false,
      plugins: {
        legend: {
          position: "top",
          labels: {
            boxWidth: 14,
            boxHeight: 14,
            font: { size: 12 },
          },
        },
        datalabels: { display: true },
      },
      scales: {
        x: {
          beginAtZero: true,
          display: false,
          max: 5000,
          title: { display: true, text: "Amount (RM) " },
          grid: { display: false },
          ticks: { font: { family: 'Inter, sans-serif', size: 11 } },
        },
        y: {
          title: { display: false, text: "Category" },
          grid: { display: false },
          ticks: {
            font: { family: 'Inter, sans-serif', size: 11 },
            callback: function (value) {
              const label = this.getLabelForValue ? this.getLabelForValue(value) : value;
              const maxLineLength = 13; // Set your fixed width (number of characters per line)
              if (typeof label === 'string' && label.length > maxLineLength) {
                // Split label into lines of maxLineLength
                const regex = new RegExp(`.{1,${maxLineLength}}`, 'g');
                return label.match(regex);
              }
              return label;
            }
          }
        },
      },
    },
    plugins: [ChartDataLabels],
  });

  //Line Chart
  // Prepare canvas and context for gradient
  const ctx = document.getElementById("expenseLineChart").getContext("2d");

  // Gradient for Total Expense (blue)
  const expenseGradient = ctx.createLinearGradient(0, 0, 0, 300);
  expenseGradient.addColorStop(0, "rgba(3,83,164,1)");
  expenseGradient.addColorStop(1, "rgba(3,83,164,0.15)");

  // Gradient for Total Budget (yellow)
  const budgetGradient = ctx.createLinearGradient(0, 0, 0, 300);
  budgetGradient.addColorStop(0, "rgba(251,191,36,1)");
  budgetGradient.addColorStop(1, "rgba(251,191,36,0.15)");

  // Gradient for dark blue


  new Chart(document.getElementById("expenseLineChart"), {
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
            anchor: 'top',
            align: 'end',
            formatter: v => `RM ${Number(v).toLocaleString('en-MY', { minimumFractionDigits: 0 })}`,
            clamp: true,
            font: { family: 'Inter, sans-serif', weight: 'bold', size: 12 },
            color: '#000',
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                const yearIndex = context.dataIndex;
                const expense = yearData[yearIndex];
                const budget = yearBudgetData[yearIndex];
                let percent = expense ? ((expense / budget) * 100).toFixed(2) : "N/A";
                return [
                  `Expense: RM ${Number(expense).toLocaleString('en-MY')}`,
                  `Budget: RM ${Number(budget).toLocaleString('en-MY')}`,
                  `Expense over Budget: ${percent}%`
                ];
              }
            }
          }
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
            anchor: 'top',
            align: 'end',
            formatter: v => `RM ${Number(v).toLocaleString('en-MY', { minimumFractionDigits: 0 })}`,
            clamp: true,
            font: { family: 'Inter, sans-serif', size: 12 },
            color: '#000',
          }
        },
      ],
    },
    options: {
      responsive: true,
      layout: {
        padding: {
          left: 40,
          right: 40,
        }
      },
      plugins: {
        legend: {
          position: "top",
          labels: {
            boxWidth: 14,
            boxHeight: 14,
            font: { family: 'Inter, sans-serif', size: 12 }
          },
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          display: false,
          max: 10000,
          title: { display: true, text: "Amount (RM)" },
          grid: { display: false },
          ticks: {
            font: {
              family: 'Inter, sans-serif',
              size: 12,
            },
          },
        },
        x: {
          title: {
            display: true, text: "Year",
            font: {
              family: 'Inter, sans-serif',
              weight: 'bold',
              size: 14
            },
            color: "#000",
          },
          grid: { display: true },
          ticks: {
            font: {
              family: 'Inter, sans-serif',
              size: 12,
            },
          },
        },
      },
    },
  });
});
</script>
