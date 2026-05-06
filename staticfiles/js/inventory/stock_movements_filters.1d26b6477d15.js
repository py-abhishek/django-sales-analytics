import { formatDate } from "../utils.js";
import { updateTable } from "./stock_movements.js";

const search_field = document.getElementById("search_field");
const date_field = document.getElementById("date_field");
const reset_filters = document.getElementById("reset_filters");
const paginationBar = document.getElementById("paginationBar");


let timer;

search_field.addEventListener("input", function () {
    clearTimeout(timer);
    if (this.value === ""){
        paginationBar.style.setProperty("display", "flex", "important");
    }
    else{
        paginationBar.style.setProperty("display", "none", "important");
    }

    timer = setTimeout(() => {
        fetchData();
    }, 300);
});


date_field.addEventListener('input', function(){
    // Hide/show pagination bar
    if (this.value === ""){
        paginationBar.style.setProperty("display", "flex", "important");
    }
    else{
        paginationBar.style.setProperty("display", "none", "important");
    }
    fetchData()
})

reset_filters.addEventListener('click', resetFilters);

function resetFilters(){
    
    paginationBar.style.setProperty("display", "flex", "important");
    if (date_field.value == "" & search_field.value == "") return;
    
    date_field.value = "";
    search_field.value = "";
    fetchData()
}
// Search Sales by Customer
function fetchData(){
    const query = search_field.value;
    const date = date_field.value;
    console.log(query);
    

    fetch(`/inventory-api/search-movements/?q=${query}&date=${date}`)
    .then(response => response.json())
    .then(data => updateTable(data));
}
