import * as charts from "../charts.js"
import * as utils from "../utils.js"


function createInvCatChart() {
        const chartContainer = document.getElementById("inventoryCategoryChart")
        const labels = utils.parseJson(document.querySelector("#inventory_cat_labels"));
        const data = utils.parseJson(document.querySelector("#inventory_cat_data"));
        let titleX = ""
        let titleY = "Value (₹)"
        let seriesName = "Product"
        let toolTipUnit = "₹"
        let tpUnitPos = "prefix"
    
        const topProductsChart = new charts.Barchart(chartContainer, labels, data, seriesName, titleX, titleY, toolTipUnit, tpUnitPos)
        topProductsChart.create()
}

createInvCatChart()


// Stock Status Distribution Chart
function createDistStockChart() {
        const chartContainer = document.querySelector("#stockDistributionChart");
        const labels = utils.parseJson(document.querySelector("#dist_stock_labels"));
        const data = utils.parseJson(document.querySelector("#dist_stock_data"));
        let seriesName = "Product"
        let toolTipUnit = "Products"
        let tpUnitPos = "suffix"
        let colors = [charts.chartColors.success, charts.chartColors.warning, charts.chartColors.danger]

        let topCategoriesChart = new charts.DonutChart(chartContainer, labels, data, seriesName, toolTipUnit, tpUnitPos, colors)
        topCategoriesChart.create()     
}

createDistStockChart()


function createTopInvProductsChart() {
    const chartContainer = document.querySelector("#TopInvProductsChart");
    const labels = utils.parseJson(document.querySelector("#top_inv_pro_labels"));
    const data = utils.parseJson(document.querySelector("#top_inv_pro_data"));
    let titleX = "Total Value (₹)"
    let seriesName = ""
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    let topProductsChart = new charts.HorizontalBarchart(chartContainer, labels, data, seriesName, titleX, toolTipUnit, tpUnitPos)
    topProductsChart.create()

}

createTopInvProductsChart()