import * as charts from "../charts.js"
import * as utils from "../utils.js";


function createRevExpTrendChart() {
    const revExpTrendChartContainer = document.querySelector("#revenueExpenseChart");
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
        labels,
        series,
        titleX,
        titleY,
        toolTipUnit,
        tpUnitPos,
        [charts.chartColors.primary, charts.chartColors.danger]
    )
    revExpTrendChart.create()

    return revExpTrendChart;
}

const revExpTrendChart = createRevExpTrendChart()

function createProfitTrendChart() {
    const profitTrendChartContainer = document.querySelector("#profitTrendChart");
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

    return profitTrendChart;
}

const profitTrendChart = createProfitTrendChart()

function createExpByCatChart() {
    const chartContainer = document.querySelector("#expenseBreakdownChart")
    const labels = utils.parseJson(document.querySelector("#exp_by_cat_labels"))
    const data = utils.parseJson(document.querySelector("#exp_by_cat_data"))

    let seriesName = "Expense"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    const expByCatChart = new charts.DonutChart(chartContainer, labels, data, seriesName, toolTipUnit, tpUnitPos)
    expByCatChart.create()

    return expByCatChart
}

const expByCatChart = createExpByCatChart()



// ***************  WORKING WITH FILTERS *************** //

// Update data on each filter
const dateBtns = document.querySelectorAll("#dateFilters .btn");

dateBtns.forEach( btn => {
    btn.addEventListener('click', function(){
        if (btn.classList.contains("active-pill")) return;

        dateBtns.forEach(b => b.classList.remove("active-pill"));
        btn.classList.add("active-pill")

        fetchData()
    })
});


function updateFilterSummary(dateRange){

    let dateRangeDict = {
        "all": "All Time",
        "6m": "6 Months",
        "1y": "1 Year",
        "2y": "2 Years"
    }

    const filterSummary = document.getElementById("filter_summary").innerHTML = `${dateRangeDict[dateRange]}`

}

function fetchData(){
    const dateBtn = document.querySelector("#dateFilters .active-pill");
    const dateRange = dateBtn.dataset.range;

    var filter = `date=${dateRange}`

    fetch(`/reports-api/rev-exp-report/?${filter}`)
    .then(response => response.json())
    .then(data => updateData(data))

    // Update showing results for (filter summary)
    updateFilterSummary(dateRange)
    }


function updateData(data){
    console.log(data)
    // Update cards
    document.getElementById("cardTotalRevenue").innerHTML = "₹ " + Math.trunc(Number(data.summary.total_revenue)).toLocaleString('en-IN');
    document.getElementById("cardTotalExpense").innerHTML = "₹ " + Math.trunc(Number(data.summary.total_expense)).toLocaleString('en-IN');
    document.getElementById("cardNetProfit").innerHTML = "₹ " + Math.trunc(Number(data.summary.net_profit)).toLocaleString('en-IN');
    document.getElementById("cardProfitMargin").innerHTML = data.summary.profit_margin;

    // Update charts

    //Revenue expense chart
    revExpTrendChart.update(
        data.revenue_expense_trend.labels,
        [{
            name: "Revenue",
            data: data.revenue_expense_trend.revenue
        },

        {
            name: "Expense",
            data: data.revenue_expense_trend.expense
        }]
    )

    // profit trend chart
    profitTrendChart.update(
        data.profit_trend.labels,
        [{
            name: "Net Profit",
            data: data.profit_trend.data
        }]
    )

    // Exp by category chart
    expByCatChart.update(
        data.exp_by_category.labels,
        data.exp_by_category.data
    )

}

// reset filters
const btnReset = document.getElementById("resetFilters");
btnReset.addEventListener("click", resetFilters)

function resetFilters(){
    const btnAllTime = document.getElementById("btnAllTime");
    if(btnAllTime.classList.contains("active-pill")) return;
    dateBtns.forEach(btn => {
        btn.classList.remove("active-pill");
        btnAllTime.classList.add("active-pill");
    })

    fetchData()
}

