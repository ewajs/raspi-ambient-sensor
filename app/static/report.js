function show(data, tempFlag, humFlag) {
  var tempData = [];
  var humData = [];
  for (let i = 0; i < data.length; i++) {
    if (tempFlag) tempData.push({ t: new Date(data[i][3]), y: data[i][1] });
    if (humFlag) humData.push({ t: new Date(data[i][3]), y: data[i][2] });
  }
  // Set charts
  if (tempFlag) {
    var tempChart = new Chart(document.getElementById("tempCanvas"), {
      type: "line",
      data: {
        datasets: [
          {
            label: "Temperatura",
            data: tempData,
            borderWidth: 1,
            borderColor: "#ff0000",
            backgroundColor: "#f79696",
            pointBackgroundColor: "#f24343",
            pointBorderColor: "#ff0000",
            pointHoverBackgroundColor: "#ff0000",
            pointHoverBorderColor: "#ffffff"
          }
        ]
      },
      options: {
        scales: {
          xAxes: [
            {
              type: "time",
              ticks: {
                autoSkip: true,
                maxTicksLimit: 30
              }
            }
          ],
          yAxes: [
            {
              display: true,
              ticks: {
                suggestedMin: 0, // minimum will be 0, unless there is a lower value.
                max: 45
              }
            }
          ]
        }
      }
    });
  }
  if (humFlag) {
    var humChart = new Chart(document.getElementById("humCanvas"), {
      type: "line",
      data: {
        datasets: [
          {
            label: "Humedad",
            data: humData,
            borderWidth: 1,
            borderColor: "#0000FF",
            backgroundColor: "#9696ff",
            pointBackgroundColor: "#3838ff",
            pointBorderColor: "#0000ff",
            pointHoverBackgroundColor: "#0000ff",
            pointHoverBorderColor: "#ffffff"
          }
        ]
      },
      options: {
        scales: {
          xAxes: [
            {
              type: "time",
              ticks: {
                autoSkip: true,
                maxTicksLimit: 20
              }
            }
          ],
          yAxes: [
            {
              display: true,
              ticks: {
                suggestedMin: 0, // minimum will be 0, unless there is a lower value.
                max: 100
              }
            }
          ]
        }
      }
    });
  }
}

show(data, report_data[1], report_data[2]);
