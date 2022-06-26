const ctx = document.getElementById('myChart').getContext('2d');
const labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'];
let insert_data_count = 0;
const datasets = [12, 19, 3, 5, 2, 3];
const config = {
    labels: labels,
    datasets: [{
        label: '# of Votes',
        data: datasets,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
}

const myChart = new Chart(ctx, {
    type: 'bar',
    data: config,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

function helloworld(){
    const backGroundColorVal=backgroundColorValue();
    const borderColorVal=borderColorValue();
    const input_elem = document.getElementById('inputID');
    const graphLabel = document.getElementById('textName');
    if(input_elem.value =='' && graphLabel.value == ''){
        alert('please input Value field and Graph Label field');
        return;
     }
    else if(input_elem.value ==''){
       alert('please input Value field');
       return;
    }
    else if(graphLabel.value == ''){
        alert('please Graph Label field');
       return;
    }
    datasets.push(parseInt(input_elem.value));
    myChart.data.datasets[0].data = datasets;
    myChart.data.datasets[0].backgroundColor.push(backGroundColorVal);
    myChart.data.datasets[0].borderColor.push(borderColorVal);
    if(graphLabel.value == undefined||graphLabel.value ==''){
    labels.push('Test' + insert_data_count);
    myChart.data.labels = labels;
    insert_data_count += 1;
    }
    else{
        labels.push(graphLabel.value);
        myChart.data.labels = labels;
    }
    myChart.update();
}

function backgroundColorValue(){
    const colorID = document.getElementById('colorID');
    const redValue = colorID.value.slice(1,3);
    const greenValue = colorID.value.slice(3,5);
    const blueValue = colorID.value.slice(5);
    const colorMapping = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    const redValueTrans = colorMapping[redValue[0]]*16+colorMapping[redValue[1]];
    const greenValueTrans = colorMapping[greenValue[0]]*16+colorMapping[greenValue[1]];
    const blueValueTrans = colorMapping[blueValue[0]]*16+colorMapping[blueValue[1]];
    return `rgba(${redValueTrans}, ${greenValueTrans}, ${blueValueTrans}, 0.2)`;
}
function borderColorValue(){
    const colorID = document.getElementById('colorID');
    const redValue = colorID.value.slice(1,3);
    const greenValue = colorID.value.slice(3,5);
    const blueValue = colorID.value.slice(5);
    const colorMapping = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    const redValueTrans = colorMapping[redValue[0]]*16+colorMapping[redValue[1]];
    const greenValueTrans = colorMapping[greenValue[0]]*16+colorMapping[greenValue[1]];
    const blueValueTrans = colorMapping[blueValue[0]]*16+colorMapping[blueValue[1]];

    return `rgba(${redValueTrans}, ${greenValueTrans}, ${blueValueTrans}, 1.0)`;
}