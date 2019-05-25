function getData() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      update(JSON.parse(this.responseText));
    }
  };
  xhttp.open("GET", "/get", true);
  xhttp.send();
  console.log("Retrieving Data...");
  setTimeout(getData, 300000);
}

function update(data) {
  var tempData = [];
  var humData = [];
  for (let i = 0; i < data.length; i++) {
    tempData.push({ t: new Date(data[i][3]), y: data[i][1] });
    humData.push({ t: new Date(data[i][3]), y: data[i][2] });
  }
  // Retrieve all last values and update h2s
  let dateValues = tempData[0].t.toString().split(" ");
  let dateString =
    dateValues[0] +
    " " +
    dateValues[1] +
    " " +
    dateValues[2] +
    " " +
    dateValues[3] +
    " " +
    dateValues[4];
  document.getElementById("lastMeasureDate").innerText = dateString;
  document.getElementById("temp").innerText = tempData[0].y;
  document.getElementById("hum").innerText = humData[0].y;
  // Set charts
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
            time: {
              unit: "minute"
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
            time: {
              unit: "minute"
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

getData();
