
const ctx = document.getElementById('myGraph');


const data = {
    labels: date,
    datasets: [{
      axis: 'y',
      label: 'My First Dataset',
      data: data1,
      borderColor: 'rgb(75, 192, 192)',
      borderWidth: 1
    }],
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
