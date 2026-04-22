import { formatDate } from "../utils.js";

const search_field = document.getElementById("search_field");
const date_field = document.getElementById("date_field");
const p_method_field = document.getElementById("p_method_field");
const btn_filter = document.getElementById("btn_filter");

search_field.addEventListener('input', function(e) {
    const query = this.value;
    console.log(query);
    searchQuery(query);

})

// Search Sales by Customer
function searchQuery(query){
    fetch(`/purchases-api/search-purchases/?q=${query}`)
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