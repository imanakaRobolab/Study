function alignCenter(){
    let flexDiv = document.querySelectorAll('div')[0];
    console.dir(flexDiv);
    const existClass = flexDiv.getAttribute('class');
    flexDiv.setAttribute('class',`flex flex-center`);
    console.log(flexDiv.getAttribute('class'));
}

function alignLeft(){
    let flexDiv = document.querySelector('div.flex');
    console.dir(flexDiv);
    console.log(flexDiv.getAttribute('class'));
    const existClass = flexDiv.getAttribute('class');
    flexDiv.setAttribute('class',`flex flex-start`);
    console.log(flexDiv.getAttribute('class'));
    
}

function alignRight(){
    let flexDiv = document.querySelector('div.flex');
    console.dir(flexDiv);
    console.log(flexDiv.getAttribute('class'));
    const existClass = flexDiv.getAttribute('class');
    flexDiv.setAttribute('class',`flex flex-end`);
    console.log(flexDiv.getAttribute('class'));
    
}

function alignBetween(){
    let flexDiv = document.querySelector('div.flex');
    console.dir(flexDiv);
    console.log(flexDiv.getAttribute('class'));
    const existClass = flexDiv.getAttribute('class');
    flexDiv.setAttribute('class',`flex flex-between`);
    console.log(flexDiv.getAttribute('class'));
    
}