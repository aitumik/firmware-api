function BuildChart(labels,values,chartTitle) {
  var data = {
    labels: labels,
    datasets: [{
      label: chartTitle,data: values,
      fillColor: "rgba(151,249,190,0.5)",
      strokeColor: "rgba(255,255,255,1)",
      pointColor: "rgba(220,220,220,1)",
      pointStrokeColor: "#fff",
      },
    ],
  };

  var ctx = document.getElementById("myChart").getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: {
      animation: {
        duration: 0,
      },
      responsive: true,
      scales: {
        xAxes: [{
          afterFit: (scale) => {
            scale.height = 120;
          },
          ticks: {
            autoSkip: true,
            maxTicksLimit: 24,
          },
          scaleLabel: {
            display: true,
            labelString: 'Time'
          }
        }],
        yAxes: [{
          ticks: {
            max: 60,
            autoSkip: true,
            min: 4,
            stepSize: 1,
          },
          scaleLabel: {
            display: true,
            labelString: "Temperature"
          }
        }]
      }
    }
  });
  return myChart;
}

var mockLabels = ["0:00:0","0:00:0","0:00:0","0:00:0","0:00:0","0:00:0"];
var mockValues = [0,0,0,0,0,0];
var chart = BuildChart(mockLabels,mockValues,"Temperature");

function addData(myChart,labels,values) {
  var d = {
    labels: labels,
    datasets: [{
      label: "Temperature",
      data: values,
      fillColor: "rgba(151,249,190,0.5)",
      strokeColor: "rgba(255,255,255,1)",
      pointColor: "rgba(220,220,220,1)",
      pointStrokeColor: "#fff",
    }],
  };
  myChart.data = d;
  myChart.update();
}


function fetch_data() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200) {
      var json = JSON.parse(this.response);
      var realJson = json['msg'];
      var labels = realJson.map(function (e) {
        return e.timestamp.split(" ")[4]
      });
      console.log(labels);
      var values = realJson.map(function (e) {
        return (e.temperature);
      });
      addData(chart,labels,values);
    }
  };

  xhttp.open('GET',"http://134.122.30.208/api/v1/data",false);
  xhttp.send();
}

setInterval(function(){
    fetch_data();
}, 1000);
