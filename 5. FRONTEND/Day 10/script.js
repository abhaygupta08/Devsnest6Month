let cardIsFlipped = false;
let boardLocked = false;
let firstCard;
let secondCard;

const card = document.querySelectorAll(".card");
// console.log(card)
function SetColor(){
    card[0].classList.add("yellow")
    card[1].classList.add("violet")
    card[2].classList.add("blue")
    card[3].classList.add("maroon")
    card[4].classList.add("orange")
    card[5].classList.add("green")

    card[6].classList.add("yellow")
    card[7].classList.add("violet")
    card[8].classList.add("blue")
    card[9].classList.add("maroon")
    card[10].classList.add("orange")
    card[11].classList.add("green")

}
function hideColor(){
    for(let i=0;i<card.length;i++){
        card[i].classList.add("hide")
    }
}
SetColor();
hideColor();

function resetCards() {
    cardIsFlipped = false;
    boardLocked = false;
    firstCard = null
    secondCard = null;
}

function disableCard(){
    firstCard.removeEventListener("click",flipCards)
    secondCard.removeEventListener("click",flipCards)
    resetCards()
}
function unflipCards(){
    boardLocked = true;
    firstCard.classList.toggle("hide")
    secondCard.classList.toggle("hide")
    restcard()
}
function flipCards() {
    // console.log(this,firstCard,secondCard)
    if (boardLocked) return;
    if (this == firstCard) return;
    this.classList.toggle("hide")

    if (!cardIsFlipped) {
        cardIsFlipped = true;
        firstCard = this;
        console.log(this.style)
        return;
    }
    secondCard = this;
    doMatch();
}

card.forEach(card => card.addEventListener("click",flipCards) )
function doMatch(){
    let matches  = firstCard.style.background == secondCard.style.background;
    if(matches){disableCard();}
    else{unflipCards()}
    
}
