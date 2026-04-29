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

// Search Expenses
function fetchData(){
    const query = search_field.value;
    const date = date_field.value;

    fetch(`/expense-api/search-expenses/?q=${query}&expense_date=${date}`)
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

    data.forEach((expense, index) => {
        const profitClass =
        parseFloat(expense.total_profit) < 0 ? "text-danger" : "text-success";

        const row = document.createElement("tr");
        row.classList.add("clickable-row");

        // dynamic URL
        row.dataset.url = `/expense/list/${expense.id}`;

        row.innerHTML = `
        <td>${index + 1}</td>
        <td>${expense.name}</td>
        <td>${formatDate(expense.expense_date)}</td>
        <td>
            ${expense.category}
        </td>
        <td>
            ₹ ${Number(expense.amount).toLocaleString("en-IN")}
        </td>
        `;

        tbody.appendChild(row);
    })
}