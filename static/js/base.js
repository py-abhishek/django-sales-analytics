const form = document.querySelector("form")
if (form !== null){
    form.addEventListener("keydown", function(e) {
        if (e.key === "Enter") {
            e.preventDefault();
        }
    })

}