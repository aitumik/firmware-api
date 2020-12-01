function BuildChart(labels,values,chartTitle) {
  var data = {
    labels: labels,
    datasets: [{
      label: chartTitle,
      data: values,
    }],
  };

  var ctx = document.getElementById("myChart").getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: {
      animation: {
        duration: 0,
      },
      backgroundColor: [
         "rgb(255, 99, 132)",
      ],
      responsive: true,
      scales: {
        xAxes: [{
          scaleLabel: {
            display: true,
            labelString: 'Time'
          }
        }],
        yAxes: [{
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

var mockLabels = ["Monday","Tuesday","Wed","Thur","Fri","Sat"];
var mockValues = [10,13,12,11,20,3];
var chart = BuildChart(mockLabels,mockValues,"Temperature");

function addData(myChart,labels,values) {
  var d = {
    labels: labels,
    datasets: [{
      label: "Temperature",
      data: values,
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

  xhttp.open('GET',"http://localhost:5000/api/v1/data",false);
  xhttp.send();
}

setInterval(function(){
    fetch_data();
}, 1000);

