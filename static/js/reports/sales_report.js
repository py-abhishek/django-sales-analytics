import * as charts from "../charts.js"
import { parseJson } from "../utils.js"

let salesTrendChart
let paymentschart
// Sales Report
function createSalesTrendChart(){

    const chartContainer = document.querySelector("#salesTrendChart");
    const labels = parseJson(document.querySelector("#sales_trend_labels"));
    const data = parseJson(document.querySelector("#sales_trend_data"));
    let titleX = "Month"
    let titleY = "Total Revenue (₹)"
    let seriesName = "Sales"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    salesTrendChart = new charts.LineChart(chartContainer, labels, data, seriesName, titleX, titleY, toolTipUnit, tpUnitPos)
    salesTrendChart.create()
}

function createPaymentChart(){
    const chartContainer = document.querySelector("#paymentChart");
    const labels = parseJson(document.querySelector("#payment_labels"));
    const data = parseJson(document.querySelector("#payment_counts"));

    paymentschart = new charts.PieChart(chartContainer, labels, data)
    paymentschart.create()

}

createSalesTrendChart();
createPaymentChart();
