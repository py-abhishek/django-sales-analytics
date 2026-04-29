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

    fetch(`/inventory-api/search-movements/?q=${query}&date=${date}`)
    .then(response => response.json())
    .then(data => updateTable(data));
}

// Update the existing table
function updateTable(data){
    const tbody = document.getElementById("tbody");
    tbody.innerHTML = "";

    if(data.length == 0) {
        tbody.innerHTML = `
        <tr>
        <td colspan='7' class="text-center">No record found</td>
        </tr>
        `;
        return;
    }

    data.forEach((sMovement, index) => {
       
        const row = document.createElement("tr");
        // row.classList.add("clickable-row");

        // // dynamic URL
        // row.dataset.url = `/inventory/list/${product.id}`;
        // ensure it's treated as a number
        const qty = Number(sMovement.quantity_change);

        let qtyClass = "";
        if (qty > 0) {
            qtyClass = "text-success";   // green
        } else if (qty < 0) {
            qtyClass = "text-danger";    // red
        }

        row.innerHTML = `
        <td>${index + 1}</td>
        <td>${sMovement.product}</td>
        <td>${formatDate(sMovement.created_at)}</td>
        <td>${sMovement.transaction_type}</td>
        <td class="${qtyClass}">
            ${Number(sMovement.quantity_change).toLocaleString("en-IN")} ${sMovement.unit}
        </td>
        <td>${Number(sMovement.before_quantity).toLocaleString("en-IN")} ${sMovement.unit}</td>
        <td>${Number(sMovement.after_quantity).toLocaleString("en-IN")} ${sMovement.unit}</td>
        `;

        tbody.appendChild(row);
    })
}