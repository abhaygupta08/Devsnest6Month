// 1. 
const isArray = (input) => typeof input == "object";
// console.log(isArray([2,5,6]));

//2
const array_clone = (input) => input.slice(0);
a = [3,5,6];
// b = array_clone(a)
// b[0]+=5
// console.log(a,b);


//3
const first = function (input,index = 0) {
    if(index<0 || input.length==0){
        return []
    }
    if(index==0) return input[0];
    return input.slice(0,index);
}
// console.log(first([7, 9, 0, -2],-3));




//4
const concatComma = function(input){
    if(input.length == 0) return "";
    let temp = "";
    for(let i=0;i<input.length;i++){
        temp += input[i]+",";
    }
    return temp.slice(0,-1);

}
// console.log(concatComma(["red","green","white"]));



//5
const freq = function(input){
    countC = new Map();
    // console.log(input.length);
    if(input.length ==0) return "";
    for(let i=0;i<input.length;i++){
        if (countC.has(String(input[i]))) countC.set(String(input[i]), countC.get(String(input[i]))+1);
        else countC.set(String(input[i]),1);
    }
    var maxE,maxC=0;
    function getVal(key,value){
        if(value>maxC){
            maxC = value;
            maxE = key;
        }
    }
    countC.forEach(getVal);
    return (maxC,maxE);
    // return countC;
    
}
console.log(freq([3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3]))