(function main(arg = 'hello'){
    // arg = typeof arg !='undefined' ?arg:'hello'; 
    console.log('hello world');
    let outputDiv=document.querySelector('.output');
    console.log(outputDiv);
    outputDiv.innerHTML =`<h1>${arg} world<\h1>`;
})('Good Morning');