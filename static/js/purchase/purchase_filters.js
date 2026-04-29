import { formatDate } from "../utils.js";

const search_field = document.getElementById("search_field");
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

    fetch(`/purchases-api/search-purchases/?q=${query}&purchase_date=${date}`)
    .then(response => response.json())
    .then(data => updateTable(data));
}

// Update the existing table
function updateTable(data){
    console.log(data);
    const tbody = document.getElementById("purchases_tbody");
    tbody.innerHTML = "";

    if(data.length == 0) {
        console.log('no data');
        tbody.innerHTML = `
        <tr>
        <td colspan='6' class="text-center">No record found</td>
        </tr>
        `;
        return;
    }

    data.forEach((sale, index) => {
       
        const row = document.createElement("tr");
        row.classList.add("clickable-row");

        // dynamic URL
        row.dataset.url = `/sales/view/${sale.id}`;

        row.innerHTML = `
        <td>${index + 1}</td>
        <td>${sale.supplier}</td>
        <td>${formatDate(sale.purchase_date)}</td>
        <td>
            ${sale.payment_method}
        </td>
        <td>
            ₹ ${Number(sale.total_amount).toLocaleString("en-IN")}
        </td>
        `;

        tbody.appendChild(row);
    })
}