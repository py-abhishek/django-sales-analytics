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