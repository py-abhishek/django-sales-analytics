import { formatDate } from "../utils.js";
import * as utils from "../utils.js";

const search_field = document.getElementById("search_field");


let timer;
search_field.addEventListener("input", function () {
    clearTimeout(timer);

    timer = setTimeout(() => {
        const query = this.value;
        searchQuery(query);
    }, 300);
});

// Search Sales by Customer
function searchQuery(query){
    utils.showSearchLoader();
    fetch(`/expense-api/search-expense-categories/?q=${query}`)
    .then(response => response.json())
    .then(data => updateTable(data))
    .finally(() => {
        utils.hideSearchLoader();
    })
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

    data.forEach((category, index) => {
       
        const row = document.createElement("tr");
        // row.classList.add("clickable-row");

        // dynamic URL
        // row.dataset.url = `/inventory/list/${category.id}`;

        row.innerHTML = `
        <td>${index + 1}</td>
        <td>${category.name}</td>
        <td>${category.description || "No description provided"}</td>
        <td>${formatDate(category.created_at)}</td>
        `;

        tbody.appendChild(row);
    })
}