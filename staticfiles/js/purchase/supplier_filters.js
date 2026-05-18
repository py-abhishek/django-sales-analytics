import { formatDate } from "../utils.js";

let timer;
search_field.addEventListener("input", function () {
    clearTimeout(timer);

    timer = setTimeout(() => {
        console.log("searching");
        
        searchQuery();
    }, 300);
});


// Search Sales by Customer
function searchQuery(query){
    fetch(`/purchases-api/search-suppliers/?q=${query}`)
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
        <td colspan='6' class="text-center">No record found</td>
        </tr>
        `;
        return;
    }

    data.forEach((supplier, index) => {
       
        const row = document.createElement("tr");
        // row.classList.add("clickable-row");

        // // dynamic URL
        // row.dataset.url = `/inventory/list/${supplier.id}`;

        row.innerHTML = `
        <td>${index + 1}</td>
        <td>${supplier.name}</td>
        <td>${supplier.phone}</td>
        <td>${supplier.email || "No email provided"}</td>
        <td>${supplier.address || "No address provided"}</td>
        `;

        tbody.appendChild(row);
    })
}