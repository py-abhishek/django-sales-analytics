import * as charts from "../charts.js"
import * as utils from "../utils.js"


function createRevExpTrendChart() {
    const revExpTrendChartContainer = document.querySelector("#revenueExpenseChart");
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
    return revExpTrendChart
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
    return topProductsChart

}



function createProfitTrendChart() {
    const profitTrendChartContainer = document.querySelector("#profitTrendChart");
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
    return profitTrendChart
}


function createExpBreakdownChart() {
    const chartContainer = document.querySelector("#expenseBreakdownChart")
    const labels = utils.parseJson(document.querySelector("#exp_breakdown_labels"))
    const data = utils.parseJson(document.querySelector("#exp_breakdown_data"))

    let seriesName = "Expense"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    const expBreakdownChart = new charts.DonutChart(chartContainer, labels, data, seriesName, toolTipUnit, tpUnitPos)
    expBreakdownChart.create()
    return expBreakdownChart
}


function createSalesTrendChart(){

    const chartContainer = document.querySelector("#salesTrendChart");
    const labels = utils.parseJson(document.querySelector("#sales_trend_labels"));
    const data = utils.parseJson(document.querySelector("#sales_trend_data"));
    let titleX = "Month"
    let titleY = "Total Revenue (₹)"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    const salesTrendChart = new charts.LineChart(
        chartContainer,
        labels,
        [{
            name: "Sale",
            data: data
        }],
        titleX,
        titleY,
        toolTipUnit,
        tpUnitPos
    )
    salesTrendChart.create()
    return salesTrendChart
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

const revExpTrendChart = createRevExpTrendChart()
const topProductsChart = createTopProductsChart()
const expBreakdownChart = createExpBreakdownChart()
const profitTrendChart = createProfitTrendChart()
const salesTrendChart = createSalesTrendChart()
const topCategoriesChart = createTopCategoriesChart()


//**************** WORKING WITH FILTERS ****************//

const yearFilter = document.getElementById("yearFilter");
// const monthFilter = document.getElementById("monthFilter");

yearFilter.addEventListener("change", fetchData)
// monthFilter.addEventListener("change", fetchData)
updateYearFilter()

function updateYearFilter(){
    yearFilter.innerHTML = "";
    let option = document.createElement("option");
    option.value = "";
    option.textContent = "All Time";

    yearFilter.appendChild(option)

    const currentYear = new Date().getFullYear();
    for (let i = 0; i < 3; i++){
        let year = currentYear - i;

        option = document.createElement("option");
        option.value = year;
        option.textContent = year;

        yearFilter.appendChild(option)
    }
}

function fetchData(){
    const year = yearFilter.value;
    // const month = monthFilter.value;
    

    var filter = `year=${year}`

    fetch(`/dashboard-api/?${filter}`)
    .then(response => response.json())
    .then(data => updateData(data))

    }


function updateData(data){
    console.log(data);

    // Update cards
    document.getElementById("cardRevenue").innerHTML = "₹ " + Math.trunc(Number(data.summary.total_revenue)).toLocaleString('en-IN')
    document.getElementById("cardExpenses").innerHTML = "₹ " + Math.trunc(Number(data.summary.total_exps)).toLocaleString('en-IN')
    document.getElementById("cardProfit").innerHTML = "₹ " + Math.trunc(Number(data.summary.net_profit)).toLocaleString('en-IN')
    document.getElementById("cardTotalSales").innerHTML = Number(data.summary.total_sales).toLocaleString('en-IN')

    // Update charts
    // Revenue expense trend chart
    revExpTrendChart.update(
        data.rev_exp_trend.labels,
        [
            {
            name: "Revenue",
            data: data.rev_exp_trend.revenue
            },

            {
                name: "Expense",
                data: data.rev_exp_trend.expense
            }
    ]
    )

    // Top products chart
    topProductsChart.update(
        data.top_selling_products.labels,
        data.top_selling_products.data
    )
    
    // Expense breakdown chart
    expBreakdownChart.update(
        data.exp_breakdown.labels,
        data.exp_breakdown.data
    )
    
    // Profit trend chart
    profitTrendChart.update(
        data.profit_trend.labels,
        [{
            "name": "Net Profit",
            "data": data.profit_trend.data
        }]
    )


    // Sales trend chart
    salesTrendChart.update(
        data.sales_trend.labels,
        [{
            "name": "Sale",
            "data": data.sales_trend.data
        }]
    )

    // Top cagtegory chart
    topCategoriesChart.update(
        data.top_categories.labels,
        data.top_categories.data
    )
}