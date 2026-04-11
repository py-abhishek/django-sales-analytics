import * as charts from "../charts.js"
import * as utils from "../utils.js"

const revExpTrendChartContainer = document.querySelector("#revenueExpenseChart");

function createRevExpTrendChart() {
    const labels = utils.parseJson(document.querySelector("#rev_exp_trend_labels"));
    const rev_data = utils.parseJson(document.querySelector("#rev_data"));
    const exp_data = utils.parseJson(document.querySelector("#exp_data"));
    
    let titleX = "Month"
    let titleY = "Revenue/Expense"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"
    let series = [
        {
            name: "Revenue",
            data: rev_data
        },

        {
            name: "Expense",
            data: exp_data
        }
    ]
    
    let revExpTrendChart = new charts.LineChart(
        revExpTrendChartContainer,
        labels, series,
        titleX,
        titleY,
        toolTipUnit,
        tpUnitPos,
        [charts.chartColors.primary, charts.chartColors.danger]
    )
    revExpTrendChart.create()
}

createRevExpTrendChart()



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

}

createTopProductsChart()



const profitTrendChartContainer = document.querySelector("#profitTrendChart");

function createProfitTrendChart() {
    const labels = utils.parseJson(document.querySelector("#profit_trend_labels"));
    const data = utils.parseJson(document.querySelector("#profit_trend_data"));
    
    let titleX = "Month"
    let titleY = "Net Profit"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"
    let series = [
        {
            name: "Net Profit",
            data: data
        }
    ]
    
    let profitTrendChart = new charts.AreaChart(
        profitTrendChartContainer,
        labels,
        series,
        titleX,
        titleY,
        toolTipUnit,
        tpUnitPos,
        [charts.chartColors.success]
    )

    profitTrendChart.create()
}

createProfitTrendChart()


function createExpBreakdownChart() {
    const chartContainer = document.querySelector("#expenseBreakdownChart")
    const labels = utils.parseJson(document.querySelector("#exp_breakdown_labels"))
    const data = utils.parseJson(document.querySelector("#exp_breakdown_data"))

    let seriesName = "Expense"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    const expBreakdownChart = new charts.DonutChart(chartContainer, labels, data, seriesName, toolTipUnit, tpUnitPos)
    expBreakdownChart.create()
}

createExpBreakdownChart()
