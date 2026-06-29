import * as charts from "../charts.js"
import * as utils from "../utils.js"

// KPI Cards

const productsCard = document.getElementById("cardTotalProducts");
const inventoryCard = document.getElementById("cardInventoryValue");
const lowStockCard = document.getElementById("cardLowStock");
const outOfStockCard = document.getElementById("cardOutofStock");
const summary = utils.parseJson(document.querySelector("#summary"));

// Animate Cards
utils.animateNumber(productsCard, summary.total_products, 800, "");
utils.animateNumber(inventoryCard, summary.inventory_value, 800, "₹ ");
utils.animateNumber(lowStockCard, summary.low_stock_count, 800);
utils.animateNumber(outOfStockCard, summary.out_of_stock_count, 800);

// Storing value as dataset
productsCard.dataset.value = summary.total_products;
inventoryCard.dataset.value = summary.inventory_value;
lowStockCard.dataset.value = summary.low_stock_count;
outOfStockCard.dataset.value = summary.out_of_stock_count;


function createInvCatChart() {
        const chartContainer = document.getElementById("inventoryCategoryChart");
        const labels = utils.parseJson(document.querySelector("#inventory_cat_labels"));
        const data = utils.parseJson(document.querySelector("#inventory_cat_data"));
        let titleX = "";
        let titleY = "Value (₹)";
        let seriesName = "Product";
        let toolTipUnit = "₹";
        let tpUnitPos = "prefix";
        let series = [{
            "name": "Product",
            "data": data
        }]
    
        const inventoryCategoryChart = new charts.Barchart(chartContainer, labels, series, titleX, titleY, toolTipUnit, tpUnitPos);
        inventoryCategoryChart.create();

        return inventoryCategoryChart;
}

const inventoryCategoryChart = createInvCatChart()


// Stock Status Distribution Chart
function createstockDistChart() {
        const chartContainer = document.querySelector("#stockDistributionChart");
        const labels = utils.parseJson(document.querySelector("#dist_stock_labels"));
        const data = utils.parseJson(document.querySelector("#dist_stock_data"));
        let seriesName = "Product"
        let toolTipUnit = "Products"
        let tpUnitPos = "suffix"
        let colors = [charts.chartColors.success, charts.chartColors.warning, charts.chartColors.danger]

        let stockDistributionChart = new charts.DonutChart(chartContainer, labels, data, seriesName, toolTipUnit, tpUnitPos, colors)
        stockDistributionChart.create()  
        
        return stockDistributionChart;
}

const stockDistributionChart = createstockDistChart()


function createTopInvProductsChart() {
    const chartContainer = document.querySelector("#TopInvProductsChart");
    const labels = utils.parseJson(document.querySelector("#top_inv_pro_labels"));
    const data = utils.parseJson(document.querySelector("#top_inv_pro_data"));
    let titleX = "Total Value (₹)"
    let seriesName = ""
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    let topProductsChart = new charts.HorizontalBarchart(chartContainer, labels, data, seriesName, titleX, toolTipUnit, tpUnitPos)
    topProductsChart.create();

    return topProductsChart;

}

const topProductsChart = createTopInvProductsChart()


const allCharts = [
    inventoryCategoryChart,
    stockDistributionChart,
    topProductsChart,
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
const categoryFilter = document.getElementById("categoryFilter");

categoryFilter.addEventListener('change', fetchData);

function updateFilterSummary(categoryName){
    const filterSummary = document.getElementById("filter_summary").innerHTML = `${categoryName}`
}

function fetchData(){
    const categoryId = categoryFilter.value
    var categoryName = categoryFilter.selectedOptions[0]?.dataset.name || "All Categories";

    var filter = `category=${categoryId}`

    fetch(`/reports-api/inventory-report/?${filter}`)
    .then(response => response.json())
    .then(data => updateData(data))

    // Update showing results for (filter summary)
    updateFilterSummary(categoryName)
    }


function updateData(data){
    
    // Update cards
    utils.animateNumber(productsCard, Number(data.summary.total_products), 600, "", "", 0, Number(productsCard.dataset.value));
    utils.animateNumber(inventoryCard, Math.trunc(Number(data.summary.inventory_value)), 600, "₹ ", "", 0, Number(inventoryCard.dataset.value));
    utils.animateNumber(lowStockCard, Math.trunc(Number(data.summary.low_stock_count)), 600, "", "", 0, Number(lowStockCard.dataset.value));
    utils.animateNumber(outOfStockCard, Math.trunc(Number(data.summary.out_of_stock_count)), 600, "", "", 0, Number(outOfStockCard.dataset.value));

    // Storing value as dataset
    productsCard.dataset.value = Number(data.summary.total_products);
    inventoryCard.dataset.value =  Math.trunc(Number(data.summary.inventory_value));
    lowStockCard.dataset.value = Math.trunc(Number(data.summary.low_stock_count));
    outOfStockCard.dataset.value = Math.trunc(Number(data.summary.out_of_stock_count));
            
    
    // Update charts
    //Inventory value by cagtegory chart
    inventoryCategoryChart.update(
        data.inv_category_value.labels,
        [{
            "name": "Product",
            "data": data.inv_category_value.data
        }]        
    )

    // Stock status distribution chart
    stockDistributionChart.update(
        data.distributed_stock.labels,
        data.distributed_stock.data
    )

    // Top Inventory Value Products chart
        topProductsChart.update(
        data.top_inventory_products.labels,
        data.top_inventory_products.data
    )


    // Update table
    updateLowStockTable(data.low_stock_products)
    updateOutOfStockTable(data.out_of_stock_products)

}

function updateLowStockTable(lowStockProducts){
    const tbody = document.getElementById("lowStock_tbody");
    tbody.innerHTML = ""

    
        if(lowStockProducts.length == 0) {
            tbody.innerHTML = `
            <tr>
            <td colspan='6' class="text-center">No record found</td>
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
                ${Number(product.reorder_level).toLocaleString("en-IN")}
            </td>
            `;
    
            tbody.appendChild(row);
        })

}


function updateOutOfStockTable(outOfStockProducts){
    const tbody = document.getElementById("outOfStock_tbody");
    tbody.innerHTML = ""

    
        if(outOfStockProducts.length == 0) {
            tbody.innerHTML = `
            <tr>
            <td colspan='6' class="text-center">No record found</td>
            </tr>
            `;
            return;
        }
    
        outOfStockProducts.forEach((product, index) => {

            const row = document.createElement("tr");

            row.innerHTML = `
            <td>${product.name}</td>
            <td class="fw-semibold text-danger">
                ${Number(product.current_stock).toLocaleString("en-IN")}
            </td>
            <td>
                ${Number(product.reorder_level).toLocaleString("en-IN")}
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
    if(categoryFilter.value === "") return;

    categoryFilter.value = "";

    fetchData()
}
