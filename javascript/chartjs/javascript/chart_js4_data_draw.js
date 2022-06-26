const ctx = document.getElementById('myChart').getContext('2d');
const labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'];
let insert_data_count = 0;
const datasets2 =[
    {
        id: 'Sales', 
        nested: {value: 1500,
        value2: 100
    }
    }, 
    {
        id: 'Purchases', 
        nested: {
            value: 500,
            value2: 100
        }
    }
];
const config = {
    // labels:['Sales','Purchases'],
    datasets: [{
        label: '売上',
        data: datasets2,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
        ],
        borderColor: [
            'rgba(255, 99, 132, 1)',
        ],
        borderWidth: 1
    }]
}

const myChart = new Chart(ctx, {
    type: 'bar',
    data: config,
   options: { 
    parsing:{
        xAxisKey: ['id','id'],
        yAxisKey: ['nested.value','nested.value2']
    }},

});



