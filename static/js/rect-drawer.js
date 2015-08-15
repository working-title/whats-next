var blueHex = '#446cb3';
var redHex = '#f64747';
var redHexArray = ['#96281B' , '#EF4836' , '#f64747'];
var blueHexArray = ['#446cb3' , '#3A539B' , '#4183D7'];

function drawSalaryBar(canvas, salary){
  var salaryBar = generateSingleBarGraph(canvas, 'salary', salary, 100000, redHex);
}

function drawEmploymentRateBar(canvas, rate){
  var rateBar = generateSingleBarGraph(canvas, 'rate', rate, 100, redHex);
}

function drawDebtBar(canvas, debt){
  var debtBar = generateSingleBarGraph(canvas, 'debt', debt, 50000, blueHex);
}

function drawHoursBarChart(canvas, less30, between3060, more60){
  var data = [
    ['<30', less30],
    ['30-60', between3060],
    ['60+', more60]
  ];
  var groups = [
    ['<30','30-60','60+']
  ];
  var hoursBar = generateStackedBarGraph(canvas, data, groups, redHexArray);
}

function drawQualificationBarChart(canvas, val1, val2, val3, val4){
  var data = [
    ['No qualification', val1],
    ['School',  val2],
    ['Bachelors degree',    val3],
    ['Degree above bachelors',    val4]
  ]
  var groups = [
    ['No qualification', 'School', 'Bachelors degree', 'Degree above bachelors']
  ];
  var debtBar = generateStackedBarGraph(canvas, data, groups, blueHexArray);
}

function generateSingleBarGraph(canvas, label, value, maxValue, color){
  return c3.generate({
    bindto: canvas,
    data: {
      columns: [
          [label, value]
      ],
      type: 'bar'
    },
    bar: {
        width: 100 // this makes bar width 100px
    },
    axis: {
      y: {
        max: maxValue,
        min: 0,
        show:false
      },
      x: {
        show:false
      }
    },
    legend: {
      show: false
    },
    color: {
      pattern: [color]
    },
    tooltip: {
      format: {
        title: function (d) { return ''},
        name: function (name, ratio, id, index) { return ''; },
        value: function (value, ratio, id) {
          var format = d3.format('$');
          return format(value);
        }
      }
    }
  });
}

function generateStackedBarGraph(canvas, data, groups, colors){
  return c3.generate({
    bindto: canvas,
    data: {
      columns: data,
      type: 'bar',
      groups: groups
    },
    bar: {
        width: 100 // this makes bar width 100px
    },
    axis: {
      y: {
        min:0,
        max:100,
        show:false
      },
      x: {
        show:false
      }
    },
    color: {
      pattern: colors
    },
    tooltip: {
      format: {
        title: function (d) { return ''},
        name: function (name, ratio, id, index) { return ''; },
        value: function (value, ratio, id) {
          var format = d3.format('$');
          return format(value);
        }
      }
    }
  });
}
