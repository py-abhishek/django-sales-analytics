// Real Time Price Calcalations 
async function getProductInfo(productId){
    const response = await fetch(`/sales/product-details/${productId}`)
    if (!response.ok){
        throw Error("Product not found")
    }
    return await response.json()
}

function calProductTotal(row){
    const price = parseFloat(row.querySelector(".price").value) || 0
    const qty = parseInt(row.querySelector(".quantity").value) || 0

    row.querySelector(".product-total").value = (price*qty).toFixed(2)
}

function calGrandTotal(){
    let grandTotal = 0
    document.querySelectorAll(".sale-row").forEach(row => {
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

const saleItemForm = document.querySelector("tbody")
saleItemForm.addEventListener("change", function(e) {
    if(e.target.classList.contains("product-select"))
    {
        const row = e.target.closest(".sale-row")
        const productId = row.querySelector(".product-select").value

        const priceField = row.querySelector(".price")
        const unitField = row.querySelector(".unit")
        
        if (!productId) return

        getProductInfo(productId)
        .then(productInfo => {
        priceField.value = productInfo.selling_price
        unitField.value = productInfo.unit
        calProductTotal(row)
        calGrandTotal()
        
        })
        .catch(error => {
            console.error("Error loading product data:", error)
        })

        // Auto adding new product rows
        const itemTable = document.getElementById("sale-items")
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

    if (e.target.classList.contains("quantity")){
        const row = e.target.closest(".sale-row")
        calProductTotal(row)
        calGrandTotal()
    }

})


// ADDING OR REMOVING PRODUCTS

function addProduct() {
    const totalForms = document.getElementById("id_items-TOTAL_FORMS")
    const formCount = parseInt(totalForms.value)

    const saleItemsContainer = document.getElementById("sale-items")
    const emptyForm = document.getElementById("empty-form").cloneNode(true)

    emptyForm.innerHTML = emptyForm.innerHTML.replace(/__prefix__/g, formCount)

    emptyForm.style.display = ""
    emptyForm.removeAttribute = "id"

    saleItemsContainer.appendChild(emptyForm)

    totalForms.value = formCount+1
}


document.getElementById("add-product").addEventListener("click", function(){ addProduct() })

document.addEventListener("click", function(e) {
    if (e.target.classList.contains("remove-product")) {
        console.log("remove product")

        const saleRow = e.target.closest(".sale-row")
        saleRow.remove()
        calGrandTotal()
    }
})