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

    fetch(`/inventory-api/search-products/?q=${query}&date=${date}`)
    .then(response => response.json())
    .then(data => updateTable(data));
}

// Update the existing table
function updateTable(data){
    const tbody = document.getElementById("products_tbody");
    tbody.innerHTML = "";

    if(data.length == 0) {
        tbody.innerHTML = `
        <tr>
        <td colspan='7' class="text-center">No record found</td>
        </tr>
        `;
        return;
    }

    data.forEach((product, index) => {
       
        const row = document.createElement("tr");
        row.classList.add("clickable-row");

        // dynamic URL
        row.dataset.url = `/inventory/list/${product.id}`;

        row.innerHTML = `
        <td>${index + 1}</td>
        <td>${product.name}</td>
        <td>${product.sku}</td>
        <td>₹ ${Math.trunc(product.current_avg_cost)}</td>
        <td>
            ₹ ${Number(product.selling_price).toLocaleString("en-IN")}
        </td>
        <td>${product.current_stock} ${product.unit}</td>
        <td>${formatDate(product.created_at)}</td>
        `;

        tbody.appendChild(row);
    })
}