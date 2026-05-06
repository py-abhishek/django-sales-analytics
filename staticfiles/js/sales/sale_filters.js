import { formatDate } from "../utils.js";

let timer;
search_field.addEventListener("input", function () {
    clearTimeout(timer);

    timer = setTimeout(() => {
        fetchData();
    }, 300);
});

const date_field = document.getElementById("date_field");
const reset_filters = document.getElementById("reset_filters");

search_field.addEventListener('input', fetchData)
date_field.addEventListener('input', fetchData)
reset_filters.addEventListener('click', resetFilters);

function resetFilters(){
    if (date_field.value == "" & search_field.value == "") return;

    date_field.value = "";
    search_field.value = "";
    fetchData()
}

// Search Sales by Customer
function fetchData(){
    const query = search_field.value;
    const date = date_field.value;

    fetch(`/sales-api/search-sales/?q=${query}&sale_date=${date}`)
    .then(response => response.json())
    .then(data => updateTable(data));
}

// Update the existing table
function updateTable(data){
    const tbody = document.getElementById("sales_tbody");
    tbody.innerHTML = "";

    if(data.length == 0) {
        tbody.innerHTML = `
        <tr>
        <td colspan='6' class="text-center">No record found</td>
        </tr>
        `;
        return;
    }

    data.forEach((sale, index) => {
        const profitClass =
        parseFloat(sale.total_profit) < 0 ? "text-danger" : "text-success";

        const row = document.createElement("tr");
        row.classList.add("clickable-row");

        // dynamic URL
        row.dataset.url = `/sales/view/${sale.id}`;

        row.innerHTML = `
        <td>${index + 1}</td>
        <td>${sale.customer}</td>
        <td>${formatDate(sale.sale_date)}</td>
        <td>
            <span class="badge-soft badge-success">
            ${sale.payment_method}
            </span>
        </td>
        <td class="fw-semibold">
            ₹ ${Number(sale.total_amount).toLocaleString("en-IN")}
        </td>
        <td class="${profitClass} fw-semibold">
            ₹ ${Math.trunc(Number(sale.total_profit)).toLocaleString("en-IN")}
        </td>
        `;

        tbody.appendChild(row);
    })
}