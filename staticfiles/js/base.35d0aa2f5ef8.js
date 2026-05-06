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

document.addEventListener("click", function (e) {
  const row = e.target.closest(".clickable-row");

  if (!row) return;

  // Ignore clicks on links or buttons
  if (e.target.closest("a, button")) return;

  if (row.dataset.url) {
    window.location = row.dataset.url;
  }
});