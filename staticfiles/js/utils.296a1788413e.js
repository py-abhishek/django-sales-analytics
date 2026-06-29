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
            timeZone: "UTC",
            year: "numeric",
            month: "long",
            day: "numeric"
        })
    }
    catch(error){
        console.log(dateStr)
        return dateStr
    }
    
}


// For chart animation on scroll
export function observeOnce(element, callback, threshold = 0.2) {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    callback(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold
        }
    );

    observer.observe(element);
}

// Function for counter
export function animateNumber(
    element,
    endValue,
    duration = 1000,
    prefix = "",
    suffix = "",
    decimals = 0,
    startValue = 0
) {
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        const value =
            startValue + (endValue - startValue) * progress;

        element.textContent =
            prefix +
            Number(value).toLocaleString("en-IN", {
                minimumFractionDigits: decimals,
                maximumFractionDigits: decimals
            }) +
            suffix;

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}