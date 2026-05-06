import { formatDate } from "../utils.js";

let timer;
search_field.addEventListener("input", function () {
    clearTimeout(timer);

    timer = setTimeout(() => {
        searchQuery(this.value);
    }, 300);
});



// Search Sales by Customer
function searchQuery(query){
    fetch(`/sales-api/search-customers/?q=${query}`)
    .then(response => response.json())
    .then(data => updateTable(data));
}

// Update the existing table
function updateTable(data){
    console.log(data);
    const tbody = document.getElementById("tbody");
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

    data.forEach((customer, index) => {
       
        const row = document.createElement("tr");
        // row.classList.add("clickable-row");

        // // dynamic URL
        // row.dataset.url = `/inventory/list/${customer.id}`;

        row.innerHTML = `
        <td>${index + 1}</td>
        <td>${customer.name}</td>
        <td>${customer.phone}</td>
        <td>${customer.email || "No email provided"}</td>
        <td>${customer.address || "No address provided"}</td>
        `;

        tbody.appendChild(row);
    })
}