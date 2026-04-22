import { formatDate } from "../utils.js";

const search_field = document.getElementById("search_field");
const date_field = document.getElementById("date_field");
const btn_filter = document.getElementById("btn_filter");

search_field.addEventListener('input', function(e) {
    const query = this.value;
    console.log(query);
    searchQuery(query);

})

// Search Sales by Customer
function searchQuery(query){
    fetch(`/inventory-api/search-products/?q=${query}`)
    .then(response => response.json())
    .then(data => updateTable(data));
}

// Update the existing table
function updateTable(data){
    console.log(data);
    const tbody = document.getElementById("products_tbody");
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