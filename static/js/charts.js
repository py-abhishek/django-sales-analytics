export const chartColors = {
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
    constructor(chartContainer, labels, series, titleX, titleY, toolTipUnit="", tpUnitPos="", colors=chartPalette) {
        this.container = chartContainer
        this.labels = labels
        this.series = series
        this.titleX = titleX
        this.titleY = titleY
        this.toolTipUnit = toolTipUnit
        this.tpUnitPos = tpUnitPos
        this.colors = colors

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
            
            series: this.series,

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

            colors: this.colors,

            tooltip: {
                y: {
                    formatter: (value) => {

                        if (this.tpUnitPos === "prefix") {
                            return this.toolTipUnit + " " + value.toLocaleString("en-IN")
                        }
                        
                        if (this.tpUnitPos === "suffix") {
                            return value.toLocaleString("en-IN") + " " + this.toolTipUnit
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

    update(labels, series) {
        this.labels = labels
        this.series = series
        this.chart.updateOptions({
            xaxis: {
                categories: labels
            },
            series: series
        })
    }
}


export class PieChart {
        constructor(chartContainer, labels, data, toolTipUnit, tpUnitPos) {
        this.container = chartContainer
        this.labels = labels
        this.data = data
        this.toolTipUnit = toolTipUnit
        this.tpUnitPos = tpUnitPos

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
            },
            
            tooltip: {
                y: {
                    formatter: (value) => {

                        if (this.tpUnitPos === "prefix") {
                                return this.toolTipUnit + " " + value.toLocaleString("en-IN")
                            }
                            
                        if (this.tpUnitPos === "suffix") {
                            return value.toLocaleString("en-IN") + " " + this.toolTipUnit
                        }

                        return value.toLocaleString("en-IN")
                    }
                }
            },
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
    constructor(chartContainer, labels, data, seriesName, titleX, toolTipUnit="", tpUnitPos="") {
        this.container = chartContainer
        this.labels = labels
        this.data = data
        this.seriesName = seriesName
        this.titleX = titleX
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
                title: { text: titleX },
                tickAmount: 5,
                labels: {
                    formatter: function (val) {
                        if (val > 100000) {
                            return (val / 100000).toLocaleString("en-IN") + " L"; // Lakh
                        }
                        return  val.toLocaleString("en-IN")
                    }
                }
            },

            dataLabels: {
                enabled: false
            },

            tooltip: {
                y: {
                    formatter: (value) => {
                        // let value = val
                        // if (val > 1000) {
                        //     value = (val / 1000).toLocaleString("en-IN") + " Thousands"// Simplify large values
                        // }

                        if (this.tpUnitPos === "prefix") {
                                return this.toolTipUnit + " " + value.toLocaleString("en-IN")
                            }
                            
                        if (this.tpUnitPos === "suffix") {
                            return value.toLocaleString("en-IN") + " " + this.toolTipUnit
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


export class Barchart {
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
                    horizontal: false,
                    borderRadius: 5,
                    barHeight: "50%",
                    borderRadiusApplication: "end"
                }
            },

            xaxis: {
                categories: labels,
                title: { text: titleX }
            },

            yaxis: {
                title: { text: titleY },
                labels: {
                    formatter: function (val) {
                        if (val > 100000) {
                            return (val / 100000).toLocaleString("en-IN") + " L" // Lakh
                        }
                        return  val.toLocaleString("en-IN")
                    }
                }
            },

            dataLabels: {
                enabled: false
            },

            tooltip: {
                y: {
                    formatter: (value) => {

                        if (this.tpUnitPos === "prefix") {
                                return this.toolTipUnit + " " + value.toLocaleString("en-IN")
                            }
                            
                        if (this.tpUnitPos === "suffix") {
                            return value.toLocaleString("en-IN") + " " + this.toolTipUnit
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
                type: "vertical",
                shadeIntensity: 0.1,
                opacityFrom: 0.7,
                opacityTo: 1,
                stops: [0, 100]
            }
            }
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

export class DonutChart {
     constructor(chartContainer, labels, data, seriesName, toolTipUnit="", tpUnitPos="", colors=chartPalette) {
        this.container = chartContainer
        this.labels = labels
        this.data = data
        this.seriesName = seriesName
        this.toolTipUnit = toolTipUnit
        this.tpUnitPos = tpUnitPos
        this.colors = colors

        this.options = {
            chart: {
                type: "donut",
                height: 320
            },

            series: data,

            labels: labels,

            colors: this.colors,

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
                        return (w.globals.seriesTotals.reduce((a, b) => a + b, 0)).toLocaleString('en-IN')
                        }
                    }
                    }
                }
                }
            },

            tooltip: {
                y: {
                formatter: (value) => {

                    if (this.tpUnitPos === "prefix") {
                            return this.toolTipUnit + " " + value.toLocaleString("en-IN")
                        }
                            
                    if (this.tpUnitPos === "suffix") {
                        return value.toLocaleString("en-IN") + " " + this.toolTipUnit
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



export class AreaChart {
    constructor(chartContainer, labels, series, titleX, titleY, toolTipUnit="", tpUnitPos="", colors=chartPalette) {
        this.container = chartContainer
        this.labels = labels
        this.series = series
        this.titleX = titleX
        this.titleY = titleY
        this.toolTipUnit = toolTipUnit
        this.tpUnitPos = tpUnitPos
        this.colors = colors

        this.options = {
            chart: {
                type: 'area',
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
            
            series: this.series,

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

            fill: {
                type: "gradient",
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.8,
                    opacityTo: 0.2,
                    stops: [0, 90, 100]
                }
            },

            colors: this.colors,

            tooltip: {
                y: {
                    formatter: (value) => {

                        if (this.tpUnitPos === "prefix") {
                            return this.toolTipUnit + " " + value.toLocaleString("en-IN")
                        }
                        
                        if (this.tpUnitPos === "suffix") {
                            return value.toLocaleString("en-IN") + " " + this.toolTipUnit
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

    update(labels, series) {
        this.labels = labels
        this.series = series
        this.chart.updateOptions({
            xaxis: {
                categories: labels
            },
            series: series
        })
    }
}