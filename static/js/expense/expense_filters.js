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
    fetch(`/expense-api/search-expenses/?q=${query}`)
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