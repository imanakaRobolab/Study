function list_study(){
    let list1 = [0,1,2,3,4,5,6];
    // someやeveryを使用する
    console.log(list1.every((value) =>  value>=0));
    console.log('every with bigger 5 '+list1.some((value,index)=>{
        return value >5;
    }));
    // reduceを使用する
    let sum = list1.reduce((previousValue,currentValue,currentIndex)=>{
        if(currentIndex % 2 == 0)
        return previousValue+ currentValue;
        else
        return previousValue
    });
    console.log(sum);


    // filterを使用する。
    let list2 = [0,2,3,1,50,3,40,20,12,31,9];

    let upper10 = list2.filter((value) => value > 10);
    console.log(upper10);

    let everRetVal = document.createElement('p');
    let list1_ever_retVal = list1.every((value) =>  value >=0);
    everRetVal.innerText = `every return value is ${list1_ever_retVal}`;
    document.body.appendChild(everRetVal);

    let someRetVal = document.createElement('p');
    let list1_some_retVal = list1.some((value) => value > 5);
    someRetVal.innerText = `some return value is ${list1_some_retVal}`;
    document.body.appendChild(someRetVal);

    let reduceRetVal = document.createElement('p');
    reduceRetVal.innerText = `reduce return value is ${sum}`;
    document.body.appendChild(reduceRetVal);

    let filterRetVal = document.createElement('p');
    let upper10Elem = upper10.join(',');
    console.log(upper10Elem);
    filterRetVal.innerText = `filter return value is [${upper10}]`;
    document.body.appendChild(filterRetVal);

    document.querySelector

}


(function main(arg = 'hello'){
    // arg = typeof arg !='undefined' ?arg:'hello'; 
    console.log('hello world');
    let outputDiv=document.querySelector('.output');
    console.log(outputDiv);
    outputDiv.innerHTML =`<h1>${arg} world<\h1>`;
    list_study();
})('Good Morning');