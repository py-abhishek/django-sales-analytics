// Real Time Cost Calcalations 
async function getProductInfo(productId){
    const response = await fetch(`/inventory/product-details/${productId}`)
    if (!response.ok){
        throw Error("Product not found")
    }
    return await response.json()
}

function calProductTotal(row){
    const cost = parseFloat(row.querySelector(".cost").value) || 0
    const qty = parseInt(row.querySelector(".quantity").value) || 0

    row.querySelector(".product-total").value = (cost*qty).toFixed(2)
}

function calGrandTotal(){
    let grandTotal = 0
    document.querySelectorAll(".purchase-row").forEach(row => {
        const rowTotal = parseFloat(row.querySelector(".product-total").value) || 0
        grandTotal += rowTotal
    });

    let total = "₹ " + grandTotal.toLocaleString('en-IN',{
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    })
    document.querySelector("#grand_total").innerHTML = total
    document.querySelector("#sub_total").innerHTML = total
}

const purchaseItemForm = document.querySelector("tbody")
purchaseItemForm.addEventListener("change", function(e) {
    if(e.target.classList.contains("product-select"))
    {
        const row = e.target.closest(".purchase-row")
        const productId = row.querySelector(".product-select").value

        const unitField = row.querySelector(".unit")
        
        if (!productId) return

        getProductInfo(productId)
        .then(productInfo => {
            unitField.value = productInfo.unit
            calProductTotal(row)
            calGrandTotal()
        
        })
        .catch(error => {
            console.error("Error loading product data:", error)
        })

        // Auto adding new product rows
        const itemTable = document.getElementById("purchase-items")
        const allProductCells = itemTable.querySelectorAll(".product-select")
        let emptyForms = 0
        for (const cell of allProductCells){
            if (!cell.value) {
                emptyForms += 1
            }
        }
        if (emptyForms < 2){
            addProduct()
        }


    }

    else if (e.target.classList.contains("quantity")){
        const row = e.target.closest(".purchase-row")
        calProductTotal(row)
        calGrandTotal()
    }

    else if (e.target.classList.contains("cost")){
        const row = e.target.closest(".purchase-row")
        calProductTotal(row)
        calGrandTotal()
    }

})


// ADDING OR REMOVING PRODUCTS

function addProduct() {
    const totalForms = document.getElementById("id_items-TOTAL_FORMS")
    const formCount = parseInt(totalForms.value)

    const purchaseItemsContainer = document.getElementById("purchase-items")
    const emptyForm = document.getElementById("empty-form").cloneNode(true)

    emptyForm.innerHTML = emptyForm.innerHTML.replace(/__prefix__/g, formCount)

    emptyForm.style.display = ""
    emptyForm.removeAttribute = "id"

    purchaseItemsContainer.appendChild(emptyForm)

    totalForms.value = formCount+1
}


document.getElementById("add-product").addEventListener("click", function(){ addProduct() })

document.addEventListener("click", function(e) {
    if (e.target.classList.contains("remove-product")) {
        console.log("remove product")

        const purchaseRow = e.target.closest(".purchase-row")
        purchaseRow.remove()
        calGrandTotal()
    }
})