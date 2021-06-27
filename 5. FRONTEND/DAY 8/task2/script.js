window.onload = function(){
// console.log(sq)
const row = document.createElement("div");
row.classList.add("row");



const sq = document.createElement("div");
sq.classList.add("sq","sq-white");
sq.setAttribute("onclick","toggleColor(this)");

for(let i =0;i<10;i++){
    row.innerHTML += sq.outerHTML;
}
const bigSq = document.querySelector(".bigSq");
    for (let i = 0; i < 10; i++) {
    bigSq.innerHTML += row.outerHTML;
    }
const sqr = document.querySelectorAll(".sq");

for(let i = 0;i<60;i++){
    let index = Math.floor(Math.random()*100);
    
    sqr[index].classList.toggle("sq-white");
    sqr[index].classList.toggle("sq-red");
}

}

const toggleColor = function (event) {
    event.classList.toggle("sq-white");
    event.classList.toggle("sq-red");
}
