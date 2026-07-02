import * as charts from "../charts.js"
import { parseJson } from "../utils.js"
import * as utils from "../utils.js"

// KPI Cards

const salesCard = document.getElementById("card_total_sales");
const revCard = document.getElementById("card_total_revenue");
const profitCard = document.getElementById("card_total_profit");
const avgOrderCard = document.getElementById("card_avg_order");
const summary = utils.parseJson(document.querySelector("#summary"));

// Animate Cards
utils.animateNumber(salesCard, summary.total_sales_count, 800, "");
utils.animateNumber(revCard, summary.total_revenue, 800, "₹ ");
utils.animateNumber(profitCard, summary.total_profit, 800, "₹ ");
utils.animateNumber(avgOrderCard, summary.avg_order_value, 800, "₹ ");

// Storing value as dataset
salesCard.dataset.value = summary.total_sales_count;
revCard.dataset.value = summary.total_revenue;
profitCard.dataset.value = summary.total_profit;
avgOrderCard.dataset.value = summary.avg_order_value;


// Sales Report
function createSalesTrendChart(){

    const chartContainer = document.querySelector("#salesTrendChart");
    const labels = parseJson(document.querySelector("#sales_trend_labels"));
    const data = parseJson(document.querySelector("#sales_trend_data"));
    let titleX = "Month"
    let titleY = "Total Revenue (₹)"
    let toolTipUnit = "₹"
    let tpUnitPos = "prefix"

    const salesTrendChart = new charts.LineChart(
        chartContainer,
        labels,
        [{
            name: "Sales",
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

function createPaymentChart(){
    const chartContainer = document.querySelector("#paymentChart");
    const labels = parseJson(document.querySelector("#payment_labels"));
    const data = parseJson(document.querySelector("#payment_counts"));
    let toolTipUnit = "Sales"
    let tpUnitPos = "suffix"

    const paymentsChart = new charts.PieChart(chartContainer, labels, data, toolTipUnit, tpUnitPos)
    paymentsChart.create()
    return paymentsChart

}

const salesTrendChart = createSalesTrendChart();
const paymentsChart = createPaymentChart();


const allCharts = [
    salesTrendChart,
    paymentsChart
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
const dateBtns = document.querySelectorAll("#dateFilters .btn");
const customerFilter = document.getElementById("customerFilter");
const paymentFilter = document.getElementById("paymentFilter")

dateBtns.forEach( btn => {
    btn.addEventListener('click', function(){
        if (btn.classList.contains("active-pill")) return;

        dateBtns.forEach(b => b.classList.remove("active-pill"));
        btn.classList.add("active-pill")

        fetchData()
    })
});

customerFilter.addEventListener('change', fetchData);
paymentFilter.addEventListener('change', fetchData);

function updateFilterSummary(dateRange, customerName, paymentMethod){

    let dateRangeDict = {
        "all": "All Time",
        "6m": "6 Months",
        "1y": "1 Year",
        "2y": "2 Years"
    }

    let paymentDict = {
        "": "All Payments",
        "cash": "Cash",
        "upi": "UPI",
        "card": "Card"
    }
    const filterSummary = document.getElementById("filter_summary").innerHTML = `${dateRangeDict[dateRange]} • ${customerName} • ${paymentDict[paymentMethod]}`

}

function fetchData(){
    utils.showLoader();
    
    const dateBtn = document.querySelector("#dateFilters .active-pill");
    const dateRange = dateBtn.dataset.range;
    const customerId = customerFilter.value
    const paymentMethod = paymentFilter.value;
    var customerName = customerFilter.selectedOptions[0]?.dataset.name || "All Customers";
    
    var filter = `date=${dateRange}&customer=${customerId}&pmethod=${paymentMethod}`

    fetch(`/reports-api/sales-report/?${filter}`)
    .then(response => response.json())
    .then(data => {
        updateData(data)
        utils.hideLoader();
        // Update showing results for (filter summary)
        updateFilterSummary(dateRange, customerName, paymentMethod)
    })
    .catch(error => {
        console.error(error);
        utils.hideLoader();
    });
    }


function updateData(data){

    // Update cards
    utils.animateNumber(salesCard, Math.trunc(Number(data.summary.total_sales_count)), 600, "", "", 0, Number(salesCard.dataset.value));
    utils.animateNumber(revCard, Math.trunc(Number(data.summary.total_revenue)), 600, "₹ ", "", 0, Number(revCard.dataset.value));
    utils.animateNumber(profitCard, Math.trunc(Number(data.summary.total_profit)), 600, "₹ ", "", 0, Number(profitCard.dataset.value));
    utils.animateNumber(avgOrderCard, Math.trunc(Number(data.summary.avg_order_value)), 600, "₹ ", "", 0, Number(avgOrderCard.dataset.value));

    // Storing value as dataset
    salesCard.dataset.value = Math.trunc(Number(data.summary.total_sales_count));
    revCard.dataset.value =  Math.trunc(Number(data.summary.total_revenue));
    profitCard.dataset.value = Math.trunc(Number(data.summary.total_profit));
    avgOrderCard.dataset.value = Math.trunc(Number(data.summary.avg_order_value));
            

    // Update charts
    //Sales chart
    salesTrendChart.update(
        data.sales_trend.labels,
        [{
            name: "Sales",
            data: data.sales_trend.data
        }]
        
    )

    // Payments chart
    paymentsChart.update(
        data.payment_methods.labels,
        data.payment_methods.count
    )

    // Update table
    updateCustomerTable(data.top_customers)

}

function updateCustomerTable(customerData){
    const tbody = document.getElementById("customer_tbody");
    tbody.innerHTML = ""

    
        if(customerData.length == 0) {
            tbody.innerHTML = `
            <tr>
            <td colspan='6' class="text-center">No record found</td>
            </tr>
            `;
            return;
        }
    
        customerData.forEach((customer, index) => {

            const row = document.createElement("tr");

            row.innerHTML = `
            <td>${customer.customer__name}</td>
            <td>
                ${Number(customer.orders).toLocaleString("en-IN")}
            </td>
            <td>
                ₹ ${Math.trunc(Number(customer.revenue)).toLocaleString("en-IN")}
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
    if(
        btnAllTime.classList.contains("active-pill") &
        customerFilter.value === "" &
        paymentFilter.value === ""
    ) return;

    customerFilter.value = "";
    paymentFilter.value = "";
    dateBtns.forEach(btn => {
        btn.classList.remove("active-pill");
        btnAllTime.classList.add("active-pill");
    })

    fetchData()
}
