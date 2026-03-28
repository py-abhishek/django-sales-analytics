
const nameField = document.getElementById("supplier-name")
const idField = document.getElementById("supplier-id")
const suggestionContainer = document.getElementById("supplier-suggestions")
const emailField = document.getElementById("supplier-email")
const phoneField = document.getElementById("supplier-phone")
const addressField = document.getElementById("supplier-address")
var existingSupplier = false

nameField.addEventListener("focusout", function() {
    setTimeout(() => {
        suggestionContainer.style.display = "none"
    }, 80)
})
nameField.addEventListener("focusin", function() {
    getSupplierData("a")
})
// Detect Typing
nameField.addEventListener("input", function(e) {
    if (existingSupplier){
        idField.value = ""
        cleanFields()
        existingSupplier = false
    }

    readOnly(false)
    const query = this.value
    getSupplierData(query)
})

function getSupplierData(query) {
    fetch( `/purchase/suppliers/search/?q=${query}`)
    .then(response => response.json())
    .then(data => showSuggestions(data))    
}

function showSuggestions(suppliers) {
    suggestionContainer.style.display = "block"
    suggestionContainer.innerHTML = ""
    
    suppliers.forEach(supplier => {
        const div = document.createElement("div")

        div.textContent = supplier.name + " (" + supplier.phone + ")"

        div.addEventListener("mousedown", function(){
            existingSupplier = true
            selectSupplier(supplier)
        })
        suggestionContainer.appendChild(div)
    })
}

function selectSupplier(suppleir) {
    // suggestionContainer.style.display = "none"

    // set value
    nameField.value = suppleir.name
    nameField.focus = false
    idField.value = suppleir.id
    phoneField.value = suppleir.phone
    emailField.value = suppleir.email
    addressField.value = suppleir.address

    readOnly(true)
}

function readOnly(choice) {
    phoneField.readOnly = choice
    emailField.readOnly = choice
    addressField.readOnly = choice
}

function cleanFields() {
    phoneField.value = ""
    emailField.value = ""
    addressField.value = ""
}