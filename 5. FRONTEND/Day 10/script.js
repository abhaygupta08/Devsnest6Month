const cards = document.querySelectorAll(".memory-card");
// console.log(cards);

let hasFlippedCard = false;
let lockBoard = false;
let firstCard,secondCard;


function flipCard() {
    if(lockBoard) return;
    if(this==firstCard) return;
    this.classList.add("flip");
    if(!hasFlippedCard){
        hasFlippedCard = true;
        firstCard = this;
    }
    else{
        hasFlippedCard = false;
        secondCard = this;
        // console.log(firstCard.dataset.color, secondCard.dataset.color);
        if(firstCard.dataset.color===secondCard.dataset.color){
            firstCard.removeEventListener('click', flipCard);
            secondCard.removeEventListener('click', flipCard);
            resetCards();

        }
        else{
            lockBoard = true;
            setTimeout(() => {
                firstCard.classList.remove('flip')
                secondCard.classList.remove('flip')
                lockBoard = false;
                resetCards();
            }, 1000);
        }
    }

}

function resetCards(){
    [hasFlippedCard,lockBoard] = [false,false];
    [firstCard,secondCard] = [null,null];
}

(function shuffleCards(){
    cards.forEach(card => {
        let randomPos = Math.floor(Math.random() * 8);
        card.style.order = randomPos;
    })
})();

cards.forEach(card => {
    card.addEventListener('click',flipCard);
});

