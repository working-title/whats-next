var scaleOptions = [5,10,15,20,25,30,35,40,45,50];
var radiusMin = 10;
var radiusMax = 100;
var circleX = 190;
var circleY = 91.5;
var colorPurple = '#9e5eff';
var colorGreen = '#00df99';

var salaryOptions = [10000,20000,30000,40000,50000,60000,70000,80000,90000];

function drawSalaryCircle(canvas, option, salary){
  var radius = 0;
  for(var i = 0; i < 10; i++){
    if(salary < salaryOptions[i]){
      radius = scaleOptions[i];
      break;
    }
  }
  if (radius == 0){
    radius = scaleOptions[9];
  }
  var color;
  if(option == 1){
    drawCircle(canvas, colorPurple, radius, circleX, circleY);
  } else {
    drawCircle(canvas, colorGreen, radius, circleX, circleY);
  }
}

function drawEmploymentRateCircle(canvas, colour, rate, x, y){
  var radius = 5;
  for(var i = 0; i < 10; i++){
    if(salary < salaryOptions[i]){
      radius = scaleOptions[i];
      break;
    }
  }
  if (radius == 0){
    radius = scaleOptions[9];
  }
  drawCircle(canvas, colour, radius, x, y);
}

function drawCircle (canvas, colour, radius, x, y){
  var ctx = canvas.getContext("2d");
  ctx.beginPath();
  ctx.arc(x,y,radius,0,2*Math.PI);
  ctx.fillStyle = colour;
  ctx.fill();
}

// function mapSalaryRange (salary) {
//   return (this - salaryMin) * (radiusMax - radiusMin) / (salaryMax - salaryMin) + radiusMax;
// }

function drawHoursChart(div, option, less30, between3060, more60) {

  var data = google.visualization.arrayToDataTable([
    ['Category', 'Hours per Week'],
    ['< 30',     less30],
    ['30-60',    between3060],
    ['60+',  more60]
  ]);
  var options;
  if(option == 1){
      options = {
      backgroundColor: '#fafafa',
      slices: [{color: '#9e5eff'}, {color: '#b787fe'}, {color: '#812ffc'}]
    };
  } else {
    options = {
      backgroundColor: '#fafafa',
      slices: [{color: '#00df99'}, {color: '#39efb6'}, {color: '#01bb81'}]
    };
  }

  var chart = new google.visualization.PieChart(div);

  chart.draw(data, options);
}

function drawQualificationChart(div, option, val1, val2, val3, val4) {

  var data = google.visualization.arrayToDataTable([
    ['Qualification', 'Level Reached'],
    ['No qualification',     val1],
    ['School',  val2]
    ['Bachelors degree',    val3],
    ['Degree above bachelors',    val4]
  ]);

  var options;
  if(option == 1){
      options = {
      backgroundColor: '#fafafa',
      slices: [{color: '#9e5eff'}, {color: '#b787fe'}, {color: '#812ffc'}, {color: '#caa6fe'}]
    };
  } else {
    options = {
      backgroundColor: '#fafafa',
      slices: [{color: '#00df99'}, {color: '#39efb6'}, {color: '#01bb81'}, {color: '#71f5cc'}]
    };
  }

  var chart = new google.visualization.PieChart(div);

  chart.draw(data, options);
}
