const mainSeats  = document.querySelector("#mainSeats");
// console.log(mainSeats);


const seat = document.createElement("div")
seat.classList.add("seat","seatNotBooked")
for(let i=0;i<20;i++)
mainSeats.innerHTML += seat.outerHTML;

const addedSeats = document.querySelectorAll(".seat")
// console.log(addedSeats)
for(let i=0;i<addedSeats.length;i++){
    addedSeats[i].onclick = function(){
        addedSeats[i].classList.toggle("seatNotBooked")
        addedSeats[i].classList.toggle("seatBooked")
        reCheckBooked()
    }
}

function reCheckBooked() {
    document.querySelector("#seatBookedStats") .innerText= document.querySelectorAll(".seatBooked").length
    document.querySelector("#seatNotBookedStats").innerText = document.querySelectorAll(".seatNotBooked").length
}