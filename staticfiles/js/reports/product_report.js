import * as charts from "../charts.js"
import * as utils from "../utils.js"

// KPI Cards

const productsCard = document.getElementById("cardTotalProducts");
const unitsCard = document.getElementById("cardUnitsSold");
const revenueCard = document.getElementById("cardProductRevenue");
const lowStockCard = document.getElementById("cardLowStock");
const summary = utils.parseJson(document.querySelector("#summary"));

// Animate Cards
utils.animateNumber(productsCard, summary.total_products, 800, "");
utils.animateNumber(unitsCard, summary.units_sold, 800, "");
utils.animateNumber(revenueCard, summary.product_revenue, 800, "₹ ");
utils.animateNumber(lowStockCard, summary.low_stock_products, 800);

// Storing value as dataset
productsCard.dataset.value = summary.total_products;
unitsCard.dataset.value = summary.units_sold;
revenueCard.dataset.value = summary.product_revenue;
lowStockCard.dataset.value = summary.low_stock_products;


function createProSalesTrendChart() {
    const trendChartContainer = document.querySelector("#productSalesTrendChart");
    const labels = utils.parseJson(document.querySelector("#product_trend_lables"));
    const data = utils.parseJson(document.querySelector("#product_trend_data"));
    let titleX = "Month"
    let titleY = "Total Units"
    let toolTipUnit = "Units"
    let tpUnitPos = "suffix"
    
    const productSalesTrendChart = new charts.LineChart(
        trendChartContainer,
        labels, 
        [{
            name: "Sales",
            data: data
        }],
        titleX,
        titleY,
        toolTipUnit,
        tpUnitPos
    )
    productSalesTrendChart.create()

    return productSalesTrendChart;
}

function createTopProductsChart() {
    const chartContainer = document.querySelector("#topProductsChart");
    const labels = utils.parseJson(document.querySelector("#top_products_labels"));
    const data = utils.parseJson(document.querySelector("#top_products_data"));
    let titleX = "Units"
    let seriesName = "Product"
    let toolTipUnit = "Units"
    let tpUnitPos = "suffix"

    const topProductsChart = new charts.HorizontalBarchart(chartContainer, labels, data, seriesName, titleX, toolTipUnit, tpUnitPos)
    topProductsChart.create()

    return topProductsChart;

}

function createTopCategoriesChart() {
    const chartContainer = document.querySelector("#categorySalesChart");
    const labels = utils.parseJson(document.querySelector("#category_labels"));
    const data = utils.parseJson(document.querySelector("#category_data"));
    let seriesName = "Product"
    let toolTipUnit = "Units"
    let tpUnitPos = "suffix"

    const topCategoriesChart = new charts.DonutChart(chartContainer, labels, data, seriesName, toolTipUnit, tpUnitPos)
    topCategoriesChart.create()

    return topCategoriesChart;

}


export const productSalesTrendChart = createProSalesTrendChart();
export const topProductsChart = createTopProductsChart();
export const topCategoriesChart = createTopCategoriesChart();


const allCharts = [
    topProductsChart,
    productSalesTrendChart,
    topCategoriesChart
];

//Animate on Scroll
document.querySelectorAll(".chart-card").forEach(card => {
    utils.observeOnce(card, (element) => {
        element.classList.add("show");
    });
});


allCharts.forEach(chart => {
    utils.observeOnce(chart.container, () => {
        chart.playAnimation();
    });
});


// ***************  WORKING WITH FILTERS *************** //

// Update data on each filter
const dateBtns = document.querySelectorAll("#dateFilters .btn");
const categoryFilter = document.getElementById("categoryFilter");

dateBtns.forEach( btn => {
    btn.addEventListener('click', function(){
        if (btn.classList.contains("active-pill")) return;

        dateBtns.forEach(b => b.classList.remove("active-pill"));
        btn.classList.add("active-pill")

        fetchData()
    })
});

categoryFilter.addEventListener('change', fetchData);

function updateFilterSummary(dateRange, categoryName){

    let dateRangeDict = {
        "all": "All Time",
        "6m": "6 Months",
        "1y": "1 Year",
        "2y": "2 Years"
    }

    const filterSummary = document.getElementById("filter_summary").innerHTML = `${dateRangeDict[dateRange]} • ${categoryName}`

}

function fetchData(){
    utils.showLoader();
    
    const dateBtn = document.querySelector("#dateFilters .active-pill");
    const dateRange = dateBtn.dataset.range;
    const categoryId = categoryFilter.value;
    var categoryName = categoryFilter.selectedOptions[0]?.dataset.name || "All Categories";

    var filter = `date=${dateRange}&category=${categoryId}`

    fetch(`/reports-api/product-report/?${filter}`)
    .then(response => response.json())
    .then(data => {
        updateData(data);
        utils.hideLoader();
        // Update showing results for (filter summary)
        updateFilterSummary(dateRange, categoryName)
    })
    .catch(error => {
        console.error(error);
        utils.hideLoader();
    });

    }


function updateData(data){

    // Update cards
    utils.animateNumber(productsCard, Math.trunc(Number(data.summary.total_products)), 600, "", "", 0, Number(productsCard.dataset.value));
    utils.animateNumber(unitsCard, Math.trunc(Number(data.summary.units_sold)), 600, "", "", 0, Number(unitsCard.dataset.value));
    utils.animateNumber(revenueCard, Math.trunc(Number(data.summary.product_revenue)), 600, "₹ ", "", 0, Number(revenueCard.dataset.value));
    utils.animateNumber(lowStockCard, Math.trunc(Number(data.summary.low_stock_products)), 600, "", "", 0, Number(lowStockCard.dataset.value));

    // Storing value as dataset
    productsCard.dataset.value = Math.trunc(Number(data.summary.total_products));
    unitsCard.dataset.value =  Math.trunc(Number(data.summary.units_sold));
    revenueCard.dataset.value = Math.trunc(Number(data.summary.product_revenue));
    lowStockCard.dataset.value = Math.trunc(Number(data.summary.low_stock_products));

    
    // Update charts
    //Product sales chart
    productSalesTrendChart.update(
        data.product_sales_trend.labels,
        [{
            name: "Sales",
            data: data.product_sales_trend.data
        }]
    )

    // Top products chart
    topProductsChart.update(
        data.top_selling_products.labels,
        data.top_selling_products.data
    )

    // Top categories chart
    topCategoriesChart.update(
        data.top_categories.labels,
        data.top_categories.data
    )

    // Update table
    updateSlowProductTable(data.slow_products)
    updateLowStockTable(data.low_stock_products)

}

function updateSlowProductTable(slowProducts){
    const tbody = document.getElementById("slowProducts_tbody");
    tbody.innerHTML = ""

    
        if(slowProducts.length == 0) {
            tbody.innerHTML = `
            <tr>
            <td colspan='6' class="text-center">No record found</td>
            </tr>
            `;
            return;
        }
    
        slowProducts.forEach((product, index) => {

            const row = document.createElement("tr");

            row.innerHTML = `
            <td>${product.product_name}</td>
            <td>
                ${Number(product.total_units_sold).toLocaleString("en-IN")}
            </td>
            <td>
                ${utils.formatDate(product.last_sale_date)}
            </td>
            `;
    
            tbody.appendChild(row);
        })

}


function updateLowStockTable(lowStockProducts){
    const tbody = document.getElementById("lowStock_tbody");
    tbody.innerHTML = ""

    
        if(lowStockProducts.length == 0) {
            tbody.innerHTML = `
            <tr>
            <td colspan='6' class="text-center">No low stock products</td>
            </tr>
            `;
            return;
        }
    
        lowStockProducts.forEach((product, index) => {

            const row = document.createElement("tr");

            row.innerHTML = `
            <td>${product.name}</td>
            <td class="text-warning fw-semibold">
                ${Number(product.current_stock).toLocaleString("en-IN")}
            </td>
            <td>
                ${product.reorder_level}
            </td>
            `;
    
            tbody.appendChild(row);
        })

}

// reset filters
const btnReset = document.getElementById("resetFilters");
btnReset.addEventListener("click", resetFilters)

function resetFilters(){
    const btnAllTime = document.getElementById("btnAllTime");

    if(btnAllTime.classList.contains("active-pill") & categoryFilter.value === "") return;

    categoryFilter.value = "";
    dateBtns.forEach(btn => {
        btn.classList.remove("active-pill");
        btnAllTime.classList.add("active-pill");
    })

    fetchData()
}
