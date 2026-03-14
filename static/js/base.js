const form = document.querySelector("form")
if (form !== null){
    form.addEventListener("keydown", function(e) {
        if (e.key === "Enter") {
            e.preventDefault();
        }
    })

}
const today = new Date();

const date = today.toLocaleDateString('en-US', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
});
document.getElementById("nav-date").innerHTML = date

// Clickable list rows

document.querySelectorAll(".clickable-row").forEach(row => {
    row.addEventListener("click", function(e) {

        if (e.target.tagName === "A" || e.target.tagName === "BUTTON") {
            return 
        }

        window.location = this.dataset.url
    })
})