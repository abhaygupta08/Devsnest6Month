var arr = [];
// console.log(localStorage.tasksAbhay)
var btn = document.getElementById("submitBtn");
btn.onclick = function(){
    var newTask = document.getElementById("taskToAdd");
    if(newTask.value.length==0 || search(newTask.value,arr)){return;}
    arr.push(String(newTask.value));
    var taskList = document.getElementById("taskList");
    taskList.innerHTML += template(newTask.value);
    newTask.value = "";
    // alert(newTask.value);
    localStorage.tasksAbhay = arr;
}

const template = (text) => "<div class='task' onclick='markAsC(this)' ondblclick='deletetask(this)'>"+text+"</div>";
// console.log(template("hello"));


const search = function (toSearch, array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] == toSearch) {
            return true;
        }
    }
    return false;
}

function markAsC(e){
    e.classList.toggle("completed")
}

var taskToAdd = document.getElementById("taskToAdd");
taskToAdd.addEventListener("keyup",function(event){
    if(event.keyCode===13){
        document.getElementById("submitBtn").click();
    }
})
const deletetask = function(event){
    event.style.display = "none";
    forDeletion = [event.innerText];
    // console.log(event.innerText);
    
    for (var i = 0; i < arr.length; i++) {

        if (arr[i] === event.innerText) {
            arr.splice(i, 1);
        }

    }

    // console.log(arr)
    localStorage.tasksAbhay = arr;
}
// console.log(localStorage.tasksAbhay)
        if(localStorage.tasksAbhay){tempArr = localStorage.tasksAbhay.split(',');
        // console.log(arr);
        for(let i=0;i<tempArr.length&&tempArr[i]!="";i++){
            arr.push(tempArr[i]);
            taskList.innerHTML += template(tempArr[i]);
        }}

const resetBtn = document.getElementById("resetAll")
resetBtn.onclick =function(){arr = []; localStorage.tasksAbhay = ""; taskList.innerHTML = "";}

const popup = document.getElementsByClassName("popup");
const closePopup = document.getElementById("closePopup");
closePopup.onclick = () => popup[0].style.display = "none";


document.querySelector(".iconZ").onclick = function(){
    const btn = document.querySelector(".darklight");
    if(btn.classList.contains("fa-moon-o")){
        btn.classList.remove("fa-moon-o");
        btn.classList.add("fa-sun-o");
    }
    else{
        btn.classList.remove("fa-sun-o");
        btn.classList.add("fa-moon-o");
    }
    document.querySelector("body").classList.toggle("darkmodeBody");
    document.getElementById("taskToAdd").classList.toggle("darkmodeInput");
    document.getElementById("submitBtn").classList.toggle("darkModeinputBtn");
}
