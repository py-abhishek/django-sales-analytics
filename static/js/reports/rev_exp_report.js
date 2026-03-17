import * as charts from "../charts.js"
import * as utils from "../utils.js"


const revExpTrendChartContainer = document.querySelector("#revenueExpenseChart");

function createRevExpTrendChart() {
    const labels = utils.parseJson(document.querySelector("#rev_exp_labels"));
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


const profitTrendChartContainer = document.querySelector("#profitTrendChart");

function createProfitTrendChart() {
    const labels = utils.parseJson(document.querySelector("#profit_labels"));
    const data = utils.parseJson(document.querySelector("#profit_data"));
    
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



function createExpByCatChart() {
    const chartContainer = document.querySelector("#expenseBreakdownChart")
    const labels = utils.parseJson(document.querySelector("#exp_by_cat_labels"))
    const data = utils.parseJson(document.querySelector("#exp_by_cat_data"))

    let seriesName = "Expense"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    const expByCatChart = new charts.DonutChart(chartContainer, labels, data, seriesName, toolTipUnit, tpUnitPos)
    expByCatChart.create()
}

createExpByCatChart()