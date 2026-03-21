console.log("working")

const nameField = document.getElementById("customer-name")
const idField = document.getElementById("customer-id")
const suggestionContainer = document.getElementById("customer-suggestions")
const emailField = document.getElementById("customer-email")
const phoneField = document.getElementById("customer-phone")
const addressField = document.getElementById("customer-address")
var existingCustomer = false

nameField.addEventListener("focusout", function() {
    setTimeout(() => {
        suggestionContainer.style.display = "none"
    }, 80)
})
nameField.addEventListener("focusin", function() {
    getCustomerData("a")
})
// Detect Typing
nameField.addEventListener("input", function(e) {
    if (existingCustomer){
        idField.value = ""
        cleanFields()
        existingCustomer = false
    }

    readOnly(false)
    const query = this.value
    getCustomerData(query)
})

function getCustomerData(query) {
    fetch( `/sales/customers/search/?q=${query}`)
    .then(response => response.json())
    .then(data => showSuggestions(data))    
}

function showSuggestions(customers) {
    suggestionContainer.style.display = "block"
    suggestionContainer.innerHTML = ""
    
    customers.forEach(customer => {
        const div = document.createElement("div")

        div.textContent = customer.name + " (" + customer.phone + ")"

        div.addEventListener("mousedown", function(){
            existingCustomer = true
            selectCustomer(customer)
        })
        suggestionContainer.appendChild(div)
    })
}

function selectCustomer(customer) {
    // suggestionContainer.style.display = "none"

    // set value
    nameField.value = customer.name
    nameField.focus = false
    idField.value = customer.id
    phoneField.value = customer.phone
    emailField.value = customer.email
    addressField.value = customer.address

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