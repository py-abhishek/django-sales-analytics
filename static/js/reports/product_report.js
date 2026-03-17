import * as charts from "../charts.js"
import * as utils from "../utils.js"

const trendChartContainer = document.querySelector("#productSalesTrendChart");

let productSalesTrendChart
let topProductsChart
let topCategoriesChart

function createProSalesTrendChart() {
    const labels = utils.parseJson(document.querySelector("#product_trend_lables"));
    const data = utils.parseJson(document.querySelector("#product_trend_data"));
    let titleX = "Month"
    let titleY = "Total Units"
    let toolTipUnit = "Units"
    let tpUnitPos = "suffix"
    
    productSalesTrendChart = new charts.LineChart(trendChartContainer, labels, [{ name: "Sales", data: data }], titleX, titleY, toolTipUnit, tpUnitPos)
    productSalesTrendChart.create()
}



function createTopProductsChart() {
    const chartContainer = document.querySelector("#topProductsChart");
    const labels = utils.parseJson(document.querySelector("#top_products_labels"));
    const data = utils.parseJson(document.querySelector("#top_products_data"));
    let titleX = "Units"
    let seriesName = "Product"
    let toolTipUnit = "Units"
    let tpUnitPos = "suffix"

    topProductsChart = new charts.HorizontalBarchart(chartContainer, labels, data, seriesName, titleX, toolTipUnit, tpUnitPos)
    topProductsChart.create()

}

function createTopCategoriesChart() {
    const chartContainer = document.querySelector("#categorySalesChart");
    const labels = utils.parseJson(document.querySelector("#category_labels"));
    const data = utils.parseJson(document.querySelector("#category_data"));
    let seriesName = "Product"
    let toolTipUnit = "Units"
    let tpUnitPos = "suffix"

    topCategoriesChart = new charts.DonutChart(chartContainer, labels, data, seriesName, toolTipUnit, tpUnitPos)
    topCategoriesChart.create()

}


createProSalesTrendChart()
createTopProductsChart()
createTopCategoriesChart()



// ************** Working with filters **************** //
const btnProductFilter = document.getElementById("btnProductFilter")

function getFilterValues() {
    const fromDateField = document.getElementById("fromDate")
    const toDateField = document.getElementById("toDate")
    const categoryField = document.getElementById("selectCategory")
    var fromDate = fromDateField.value
    var toDate = toDateField.value
    var category  = categoryField.value

    return {
        fromDate: fromDate,
        toDate: toDate,
        category: category
    }
}

btnProductFilter.addEventListener("click", function() {
    const filterValues = getFilterValues()
    if (!filterValues) return

    getFilteredData(filterValues)
    .then(data => {
        console.log(data)
        updateCharts(data)
        updateCardsTables(data)
    })
})

function getFilteredData(filterValues) {

    // calling function from utils file
    return utils.fetchWithCSRF(
            "/reports/product/filter-data",
            filterValues,
            "POST"
        )
        .catch(error => console.log(error))
    
}

function updateCharts(data) {
    let proSaleTrend = {
        labels: data['product_sales_trend']['labels'],
        data: data['product_sales_trend']['data']
    }

    let topSellingProducts = {
        labels: data['top_selling_products']['labels'],
        data: data['top_selling_products']['data']
    }

    let topCategories = {
        labels: data['top_categories']['labels'],
        data: data['top_categories']['data']
    }
    productSalesTrendChart.update(proSaleTrend['labels'], proSaleTrend['data'])
    topProductsChart.update(topSellingProducts['labels'], topSellingProducts['data'])
    topCategoriesChart.update(topCategories['labels'], topCategories['data'])

    if (!data.summary.total_products){
        trendChartContainer.innerHTML = "No data available for selected filter."
    }
}

function updateCardsTables(data) {
    const cardTotalProducts = document.getElementById("cardTotalProducts")
    const cardUnitsSold = document.getElementById("cardUnitsSold")
    const cardProductRevenue = document.getElementById("cardProductRevenue")
    const cardLowStock = document.getElementById("cardLowStock")

    const resultForDate = document.getElementById("resultFor_date")
    const resultForCat = document.getElementById("resultFor_category")

    const tableSlowProducts = document.getElementById("tableSlowProducts")

    let fromDate = utils.formatDate(data.results_for.date.from)
    let toDate = utils.formatDate(data.results_for.date.to)

    // // updating showing filter for section
    resultForDate.innerHTML = "Date: " + fromDate + " – " + toDate
    resultForCat.innerHTML = "Category: " + data.results_for.category

    const summary = data.summary || {}
    // Updating Cards
    cardUnitsSold.innerHTML = (summary.units_sold || 0).toLocaleString('en-IN')
    cardProductRevenue.innerHTML = "₹" + " " + (summary.product_revenue || 0).toLocaleString('en-IN')
    cardTotalProducts.innerHTML = (summary.total_products || 0).toLocaleString('en-IN') || 0
    cardLowStock.innerHTML = (summary.low_stock_products || 0).toLocaleString('en-IN') || 0

    // Updating Slow Product Table
    tableSlowProducts.innerHTML = ""

    let slowProducts = data.slow_products || {}

    if(!slowProducts){
        tableSlowProducts.innerHTML = "No slow moving products"
    }

    slowProducts.forEach(product => {
        tableSlowProducts.innerHTML += 
        `
        <tr>
            <td>${product.product_name}</td>
            <td>${product.total_units_sold}</td>
            <td>${product.last_sale_date}</td>
        </tr>
        `
    });
}