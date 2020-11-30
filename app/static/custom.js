$(document).ready(function() {
  var dataPoints = [];
  var options = {
    theme: "light2",
    title: {
      text: "Live Data"
    },
    data: [{
      type: "line",
      dataPoints: dataPoints
    }]
  };

  $("#chartContainer").CanvasJSChart(options);
  updateData();

  //initial values
  var xValue = 19;
  var yValue = 19;
  var newDataCount = 6;


  function addData(data) {
    if(newDataCount != 1) {
      $.each(data,function(key,value) {
        dataPoints.push({x: data[0][0], y: parseInt(data[0][1])});
        xValue++;
        yValue = parseInt(data[0][1]);
      });
  } else {
    dataPoints.push({x: data[0][0], y: parseInt(data[0][1])});
    xValue++;
    yValue = parseInt(data[0][1]);
  }

    new dataCount = 1;
    $("#chartContainer").CanvasJSChart().render()
    setTimeout(updateData,1500);
  }

  functionUpdateData() {

  }

});
