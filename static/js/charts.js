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

export class LineChart {
    constructor(chartContainer, labels, data, seriesName, titleX, titleY, toolTipUnit="", tpUnitPos="") {
        this.container = chartContainer
        this.labels = labels
        this.data = data
        this.seriesName = seriesName
        this.titleX = titleX
        this.titleY = titleY
        this.toolTipUnit = toolTipUnit
        this.tpUnitPos = tpUnitPos

        this.options = {
            chart: {
                type: 'line',
                height: 350,
                toolbar: {
                    show: false
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                    dynamicAnimation: {
                        enabled: true,
                        speed: 800
                    }
                },
            },
            
            series: [{
                name: this.seriesName,
                data: this.data
            }],

            xaxis: {
                categories: this.labels,
                title: {
                    text: this.titleX
                }
            },

            yaxis: {
                title: {
                    text: this.titleY
                },
                labels: {
                    formatter: function(value) {
                        return value.toLocaleString("en-IN")
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
                        const tpUnitPos = this.tpUnitPos
                        const toolTipUnit = this.toolTipUnit

                        if (tpUnitPos === "prefix") {
                            return toolTipUnit + " " + value.toLocaleString("en-IN")
                        }
                        
                        if (tpUnitPos === "suffix") {
                            return value.toLocaleString("en-IN") + " " + toolTipUnit
                        }

                        return value.toLocaleString("en-IN")
                    }
                }
            },
            
            grid: {
                borderColor: chartUI["grid"],
                strokeDashArray: 3
            },

            dataLabels: {
                enabled: false
            },

            markers: {
                size: 0,
                hover: {
                    size: 6
                }
            },
        }
    }

    create() {
        this.chart = new ApexCharts(this.container, this.options);
        this.chart.render();
    }

    update(labels, data) {
        this.labels = labels
        this.data = data
        this.chart.updateOptions({
            xaxis: {
                categories: labels
            },
            series: [{
                name: this.seriesName,
                data: data
            }]
        })
    }
}


export class PieChart {
        constructor(chartContainer, labels, data) {
        this.container = chartContainer
        this.labels = labels
        this.data = data

        this.options = {
            chart: {
                type: 'pie',
                height: 350
            },
            colors: chartPalette,
            series: data,
            labels: labels,
            legend: {
                position: 'bottom'
            }
        };
    }

    create() {
        this.chart = new ApexCharts(this.container, this.options);
        this.chart.render();
    }

    update(labels, data) {
        this.labels = labels
        this.data = data
        this.chart.updateOptions({
            labels: labels,
            series: data
        })
    }
}

export class HorizontalBarchart {
    constructor(chartContainer, labels, data, seriesName, titleX, titleY, toolTipUnit="", tpUnitPos="") {
        this.container = chartContainer
        this.labels = labels
        this.data = data
        this.seriesName = seriesName
        this.titleX = titleX
        this.titleY = titleY
        this.toolTipUnit = toolTipUnit
        this.tpUnitPos = tpUnitPos

        this.options = {
            chart: {
                type: "bar",
                height: 350,
                toolbar: { show: false }
            },

            series: [{
                name: seriesName,
                data: data
            }],

            colors: chartPalette,

            plotOptions: {
                bar: {
                    horizontal: true,
                    borderRadius: 5,
                    barHeight: "50%",
                    borderRadiusApplication: "end"
                }
            },

            xaxis: {
                categories: labels,
                title: { text: titleX }
            },

            dataLabels: {
                enabled: false
            },

            tooltip: {
                y: {
                    formatter: function(value) {
                        const toolTipUnit = this.toolTipUnit
                        const tpUnitPos = this. tpUnitPos

                        if (tpUnitPos === "prefix") {
                                return toolTipUnit + " " + value.toLocaleString("en-IN")
                            }
                            
                        if (tpUnitPos === "suffix") {
                            return value.toLocaleString("en-IN") + " " + toolTipUnit
                        }

                        return value.toLocaleString("en-IN")
                    }
                }
            },

            grid: {
                strokeDashArray: 3
            },

            fill: {
            type: "gradient",
            gradient: {
                shade: "light",
                type: "horizontal",
                shadeIntensity: 0.1,
                opacityFrom: 1,
                opacityTo: 0.7,
                stops: [0, 100]
            }
            }
        };
    }

    create() {
        this.chart = new ApexCharts(this.container, this.options);
        this.chart.render();
    }

    update(labels, data) {
        this.labels = labels
        this.data = data
        this.chart.updateOptions({
            xaxis: {
                categories: labels
            },
            series: [{
                name: this.seriesName,
                data: data
            }]
        })
    }
}

export class DonutChart {
     constructor(chartContainer, labels, data, seriesName, toolTipUnit="", tpUnitPos="") {
        this.container = chartContainer
        this.labels = labels
        this.data = data
        this.seriesName = seriesName
        this.toolTipUnit = toolTipUnit
        this.tpUnitPos = tpUnitPos

        this.options = {
            chart: {
                type: "donut",
                height: 320
            },

            series: data,

            labels: labels,

            colors: chartPalette,

            legend: {
                position: "bottom"
            },

            dataLabels: {
                enabled: false
            },

            plotOptions: {
                pie: {
                donut: {
                    size: "65%",
                    labels: {
                    show: true,

                    total: {
                        show: true,
                        label: "Total",
                        formatter: function(w) {
                        return w.globals.seriesTotals.reduce((a, b) => a + b, 0)
                        }
                    }
                    }
                }
                }
            },

            tooltip: {
                y: {
                formatter: function(value) {
                    const toolTipUnit = this.toolTipUnit
                    const tpUnitPos = this.tpUnitPos

                    if (tpUnitPos === "prefix") {
                            return toolTipUnit + " " + value.toLocaleString("en-IN")
                        }
                            
                    if (tpUnitPos === "suffix") {
                        return value.toLocaleString("en-IN") + " " + toolTipUnit
                    }

                    return value.toLocaleString("en-IN")
                }
                }
            },

            stroke: {
                width: 2
            }
        };
    }

    create() {
        this.chart = new ApexCharts(this.container, this.options);
        this.chart.render();
    }

    update(labels, data) {
        this.labels = labels
        this.data = data
        this.chart.updateOptions({
            labels: labels,
            series: data
        })
    }
}

export function donutChart(chartContainer, labels, data, seriesName, titleX, toolTipUnit="", tpUnitPos="") {
    var options = {
    chart: {
        type: "donut",
        height: 320
    },

    series: data,

    labels: labels,

    colors: chartPalette,

    legend: {
        position: "bottom"
    },

    dataLabels: {
        enabled: false
    },

    plotOptions: {
        pie: {
        donut: {
            size: "65%",
            labels: {
            show: true,

            total: {
                show: true,
                label: "Total",
                formatter: function(w) {
                return w.globals.seriesTotals.reduce((a, b) => a + b, 0)
                }
            }
            }
        }
        }
    },

    tooltip: {
        y: {
        formatter: function(value) {
            if (tpUnitPos === "prefix") {
                    return toolTipUnit + " " + value.toLocaleString("en-IN")
                }
                    
            if (tpUnitPos === "suffix") {
                return value.toLocaleString("en-IN") + " " + toolTipUnit
            }

            return value.toLocaleString("en-IN")
        }
        }
    },

    stroke: {
        width: 2
    }
    };

    var chart = new ApexCharts(chartContainer, options);
    chart.render();
}