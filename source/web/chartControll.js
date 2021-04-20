var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Red'],
        datasets: [{
            label: '# of Votes',
            data: [0],
            lineTension: 0,
            //cubicInterpolationMode: 'monotone',
            backgroundColor: '#13A3A4',
            borderColor: '#3A3A3A',
            borderWidth: 1
        }]
    },
    plugins: {
        beforeDraw: function (chart, easing) {
          var ctx = chart.chart.ctx;
          ctx.save();
          ctx.fillStyle = "#ffffff";
          ctx.fillRect(0, 0, chart.width, chart.height);
          ctx.restore();
        }
      },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

function addData(label, y) {
    myChart.data.labels.push(label)
    myChart.data.datasets[0]['data'].push(y)
    myChart.update()
}

function GsetData(labels, ys) {
   myChart.data.labels = labels;
   myChart.data.datasets[0]['data'] = ys;
   myChart.update()
}

function export_chart() {
   var a = document.createElement('a');
   a.href = myChart.toBase64Image();
   a.download = 'chart.png';

// Trigger the download
   a.click();
}
document.getElementById("exportchartimg").addEventListener("click", export_chart);

function getDataNow() {
    d = eel.getDataNow()(handleRespData);
}
document.getElementById("getDataNow").addEventListener("click", getDataNow);

var DATA = null;
function handleRespData(data) {
    DATA = data
}