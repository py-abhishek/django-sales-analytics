console.log("pagination.js loaded");

import { formatDate } from "../utils.js";   

const prevPageBtn = document.getElementById("prevPageBtn");
const nextPageBtn = document.getElementById("nextPageBtn");
const activePage = document.getElementById("activePage");
const currentPage = document.getElementById("currentPage");
const totalPages = document.getElementById("totalPages");

nextPageBtn.addEventListener('click', function(){
    console.log("Next clicked");
    let currentPageNo = Number(activePage.textContent)
    if (currentPageNo === Number(totalPages.textContent)) return;

    currentPageNo += 1;
    activePage.textContent = currentPageNo;
    currentPage.textContent = currentPageNo;
    
    fetchData(currentPageNo);
})

prevPageBtn.addEventListener('click', function(){
    let currentPageNo = Number(activePage.textContent)
    if (currentPageNo < 2) return;
    currentPageNo -= 1;
    activePage.textContent = currentPageNo;
    currentPage.textContent = currentPageNo;
    
    fetchData(currentPageNo);
})

function fetchData(activePage){
    fetch(`/inventory-api/stock-movements/?c_page=${activePage}`)
    .then(response => response.json())
    .then(data => updateTable(data.data, data.current_page));
}


// Update the existing table
export function updateTable(data, currentPage=NaN){
    // console.log(data);
    
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

        if (currentPage){
            index = index + ((currentPage-1)*100)
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