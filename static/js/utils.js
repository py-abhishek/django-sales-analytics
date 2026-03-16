export function parseJson(data){
    return JSON.parse(data.textContent)
}

export function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

export function fetchWithCSRF(url, data = {}, method = "POST") {
    return fetch(url, {
        method: method,
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json());
}


// custom date
export function formatDate(dateStr){
    try{
        const date = new Date(dateStr)

        if (isNaN(date.getTime())){
            return dateStr
        }
        
        return date.toLocaleDateString("en-US", {
            year: "numeric",
            month: "short",
            day: "numeric"
        })
    }
    catch(error){
        console.log(dateStr)
        return dateStr
    }
    
}
