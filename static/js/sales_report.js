const chartColors = {
  primary: "#4F46E5",   // Indigo - main sales trend
  success: "#22C55E",   // Green - profit / growth
  warning: "#F59E0B",   // Amber - alerts / moderate values
  danger: "#EF4444",    // Red - loss / negative
  info: "#06B6D4",      // Cyan - secondary data
  purple: "#8B5CF6",    // additional category
  teal: "#14B8A6",      // category / secondary
  orange: "#F97316"     // highlight
};


const chartPalette = [
    "#4F46E5",
    "#22C55E",
    "#06B6D4",
    "#F59E0B",
    "#EF4444",
    "#8B5CF6",
    "#14B8A6",
    "#F97316"
  ];

const chartUI = {
  grid: "#d8dbe1",
  text: "#6B7280",
  tooltipBg: "#111827",
  cardBg: "#FFFFFF",
  pageBg: "#F9FAFB"
};

function parseJson(data){
    return JSON.parse(data.textContent)
}

// Sales trend chart
function salesTrendChart(){

    const chartContainer = document.querySelector("#salesTrendChart");
    const labels = parseJson(document.querySelector("#sales_trend_labels"));
    const data = parseJson(document.querySelector("#sales_trend_data"));

    var options = {
        chart: {
            type: 'line',
            height: 350,
            toolbar: {
                show: false
            },
            animations: {
                enabled: true,
                easing: "easeinout",
                speed: 800
            },
        },
        
        series: [{
            name: 'Sales',
            data: data
        }],

        xaxis: {
            categories: labels,
            title: {
                text: "Month"
            }
        },

        yaxis: {
            title: {
                text: "Total Revenue (₹)"
            },
            labels: {
                formatter: function(value) {
                    return "₹ " + value.toLocaleString()
                }
            }
        },

        stroke: {
            curve: "smooth",
            width: 3
        },

        colors: [chartColors.primary],

        tooltip: {
            y: {
                formatter: function(value){
                    return "₹ " + value.toLocaleString()
                }
            }
        },
        
        grid: {
            borderColor: chartUI["grid"],
            strokeDashArray: 3
        },

        dataLables: {
            enabled: false
        },

        markers: {
            size: 0,
            hover: {
                size: 6
            }
        },

    };

    var chart = new ApexCharts(chartContainer, options);
    chart.render();
}

// Payment Methods Chart

function paymentChart(){
    const chartContainer = document.querySelector("#paymentChart");
    const labels = parseJson(document.querySelector("#payment_labels"));
    const counts = parseJson(document.querySelector("#payment_counts"));

    var options = {
        chart: {
            type: 'pie',
            height: 350
        },
        colors: chartPalette,
        series: counts,
        labels: labels,
        legend: {
            position: 'bottom'
        }
    };

    var chart = new ApexCharts(chartContainer, options);
    chart.render();

}


salesTrendChart();
paymentChart();


