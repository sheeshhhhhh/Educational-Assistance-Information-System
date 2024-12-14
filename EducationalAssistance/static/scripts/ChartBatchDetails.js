const getChartOptions = () => {
    return {
      series: [10, 100],
      colors: ["#1C64F2", "#16BDCA"],
      chart: {
        height: 150,
        width: "100%",
        type: "donut",
      },
      stroke: {
        colors: ["transparent"],
        lineCap: "",
      },
      plotOptions: {
        pie: {
          donut: {
            labels: {
              show: true,
              name: {
                show: true,
                fontFamily: "Inter, sans-serif",
                offsetY: 20,
              },
              total: {
                showAlways: true,
                show: true,
                label: "Current Number",
                fontSize: "10px",
                fontFamily: "Inter, sans-serif",
                formatter: function (w) {
                    const currentCount = w.globals.seriesTotals[0]
                    const limitCount = w.globals.seriesTotals[1]

                    return currentCount + "/" + limitCount
                },
              },
              value: {
                show: true,
                fontFamily: "Inter, sans-serif",
                offsetY: -20,
                formatter: function (value) {
                  return value
                },
              },
            },
            size: "80%",
          },
        },
      },
      yaxis: {
        labels: {
          formatter: function (value) {
            return value + "k"
          },
        },
      },
      xaxis: {
        labels: {
          formatter: function (value) {
            return value  + "k"
          },
        },
        axisTicks: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
      },
    }
}

if (document.getElementById("donut-chart") && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(document.getElementById("donut-chart"), getChartOptions());
    chart.render();
}