questionJSON = QUESTIONS = [
    {
        "name": " India's largest city by population",
        "option1": "Delhi",
        "option2": "Mumbai",
        "option3": "Pune",
        "option4": "Bangalore",
        "answer": 2
    },
    {
        "name": "India is a federal union comprising twenty-nine states and how many union territories?",
        "option1": "6",
        "option2": "7",
        "option3": "8",
        "option4": "9",
        "answer": 2
    },
    {
        "name": "What are the major languages spoken in Andhra Pradesh?",
        "option1": " English and Telugu",
        "option2": "Telugu and Urdu",
        "option3": "Telugu and Kannada",
        "option4": "All of the above languages",
        "answer": 2
    },
    {

        "name": "What is the state flower of Haryana?",
        "option1": "Lotus",
        "option2": "Rhododendron",
        "option3": "Golden Shower",
        "option4": "Not declared",
        "answer": 2
    },
    {

        "name": " Where was the International Conference on 'Yoga for Diabetes' organized from January 4-6, 2017?",
        "option1": "New Delhi ",
        "option2": "Jharkhand",
        "option3": "Jammu and Kashmir",
        "option4": "Haryana",
        "answer": 1
    },
    {


        "name": "Name the tower which was lighted up in Tricolour of India on Republic Day, 2017?",
        "option1": "WTC Towers",
        "option2": "Jeddah Tower",
        "option3": "Burj Khalifa",
        "option4": "Burj Al Arab",
        "answer": 3
    },
    {

        "name": "Which of the following states is not located in the North?",
        "option1": "Himachal Pradesh",
        "option2": "Jharkhand",
        "option3": "Jammu and Kashmir",
        "option4": "Haryana",
        "answer": 2
    },
    {
        "name": "In what state is the Elephant Falls located?",
        "option1": "Meghalaya",
        "option2": "Mizoram",
        "option3": "Orissa",
        "option4": "Manipur",
        "answer": 2
    },
    {
        "name": "Which state has the largest population?",
        "option1": "Maharastra",
        "option2": "Uttar Pradesh",
        "option3": "Bihar",
        "option4": "Andra Pradesh",
        "answer": 2
    },
    {
        "name": " Which state has the largest area?",
        "option1": "Maharashtra",
        "option2": "Rajasthan",
        "option3": "Bihar",
        "option4": "Andra Pradesh",
        "answer": 2
    },
    {
        "name": "Which is the largest coffee producing state of India?",
        "option1": "Maharastra",
        "option2": "Karnataka",
        "option3": "Maharashtra",
        "option4": "Rajasthan",
        "answer": 2
    },
    {
        "name": "In which state is the main language Khasi?",
        "option1": "Nagaland",
        "option2": "Rajasthan",
        "option3": "Maharashtra",
        "option4": "Meghalaya",
        "answer": 4
    },
    {

        "name": "Which of the following created history in 2016 by winning all three gold medals on offer in the 1st Western Asia Youth Chess Championship?",
        "option1": "Nihal Sarin",
        "option2": "Kush Bhagat",
        "option3": "Praggnanandhaa",
        "option4": "Vidit Gujrathi",
        "answer": 2
    },
    {


        "name": " Which Bollywood actress is the new ambassador for Swachh Bharat Mission's youth-based 'Swachh Saathi' programme?",
        "option1": "Vidya Balan ",
        "option2": "Dia Mirza ",
        "option3": "Priyanka Chopra",
        "option4": "Sonakshi Sinha",
        "answer": 2
    },
    {
        "name": "When is the Indian Air Force Day celebrated?",
        "option1": "October 9",
        "option2": "October 10",
        "option3": "October 8",
        "option4": "October 11",
        "answer": 3
    }

]


const totalQuestions = document.querySelector("#totalQuestions");
totalQuestions.innerHTML = questionJSON.length

const question = document.querySelector("#question")
const option = document.querySelectorAll(".option")

let currQ = 01
let score = 00



function updateQuestion(){
    // console.log(currQ,score,)
    document.querySelector("#currentQ").innerHTML = (currQ<10)?'0'+currQ:currQ;
    document.querySelector("#yourScore").innerHTML = (score < 10) ? '0' + score : score;
    question.innerHTML = questionJSON[currQ-1]["name"]
    for(let i =0;i<option.length;i++){
        option[i].innerHTML = questionJSON[currQ-1]["option"+String(i+1)]
        option[i].onclick = function(){
            // console.log(option[i].innerText)
            // console.log(i, questionJSON[currQ - 1]["answer"] - 1)
            let tt = i == questionJSON[currQ-1]["answer"]-1
            renderScore(tt)
        }
    };
}

function renderScore(boole){
    if(boole){
        score++;
        // toast("Correct Answer","correct")
    }
    else{
        // toast("Incorrect Answer", "incorrect")
    }
    currQ++;
    if(currQ==16){
        document.querySelector("section").remove()
        document.querySelector("main").innerHTML = `
                <div class="endStats">
            <h3>WELL PLAYED</h3><br>
            <h2>YOUR FINAL SCORE :</h2>
            <span id="finalScore">${score}</span>
        </div>
        `
        document.querySelector("main").style.backgroundColor = "#1f1f1f";
        document.querySelector("main").style.color = "white";

        document.querySelector("main").classList.add("endStatsMain");
        document.querySelector("header").style.marginBottom = "0px";
        return;
    }
    updateQuestion()
}

function toast(msg,msgtype){
    document.querySelector(".popupBox").innerHTML = `
    <h3 class="${msgtype}">${msg}</h3>
    `;
    let toastM = setInterval(() => {
        document.querySelector('.popupBox').remove();
        clearInterval(toastM);
    }, 2000);
}
updateQuestion()