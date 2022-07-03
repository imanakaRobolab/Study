function onClickFunc(){
    const inputText = document.getElementById('newTodo');
    console.log(inputText.value);
    const addTodo = inputText.value;
    inputText.value ='';
    
    const todoList = document.getElementById('TODO');
    console.dir(todoList.childElementCount);
    console.dir(todoList.childNodes);
    console.dir(todoList.children);
    const addList = document.createElement('li');
    addList.innerHTML = addTodo;
    todoList.append(addList);
    // const 
    
}

function onClickFuncRemove(){
    const todoList  = document.getElementById('TODO');
    const liList = todoList.children;
    const getIndex = document.getElementById('indexID');
    // console.log(liList);
    todoList.removeChild(liList[parseInt(getIndex.value)]);
    // todoList.removeChild(todoList.lastChild);
    // liList.shift();
}