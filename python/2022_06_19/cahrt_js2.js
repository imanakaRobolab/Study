
const ctx = document.getElementById('myGraph');


const data = {
    labels: data1,
    datasets: [{
      axis: 'y',
      label: 'open',
      data: open1,
      borderColor: 'red',
      borderWidth: 1
    },
    {
      axis: 'y',
      label: 'high',
      data: high1,
      borderColor: 'blue',
      borderWidth: 1
    },
    {
      axis: 'y',
      label: 'low',
      data: low1,
      borderColor: 'green',
      borderWidth: 1
    },
    {
      axis: 'y',
      label: 'close',
      data: close1,
      borderColor: 'rgb(75, 192, 192)',
      borderWidth: 1
    }
  
  ],
};


const config = {
    type: 'line',
    data:data,
    options: {

        scales: {
          x: {
            beginAtZero: true
          }
        }
      }
}
const myChart = new Chart(ctx, config);
