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
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    salesTrendChart = new charts.LineChart(chartContainer, labels, [{ name: "Sales", data: data }], titleX, titleY, toolTipUnit, tpUnitPos)
    salesTrendChart.create()
}

function createPaymentChart(){
    const chartContainer = document.querySelector("#paymentChart");
    const labels = parseJson(document.querySelector("#payment_labels"));
    const data = parseJson(document.querySelector("#payment_counts"));
    let toolTipUnit = "Sales"
    let tpUnitPos = "suffix"

    paymentschart = new charts.PieChart(chartContainer, labels, data, toolTipUnit, tpUnitPos)
    paymentschart.create()

}

createSalesTrendChart();
createPaymentChart();
