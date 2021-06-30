async function dataAA(){
    const data = await fetch("https://api.github.com/users/abhaygupta08")
    res = await data.json();
    console.log(res);

}
//dataAA()
async function getSheet(){
    let data = await fetch("https://sheet.best/api/sheets/e0955054-83b8-4f7d-a6ec-c919d09f7638");
    data = await data.json();
    console.log(data);
}
// getSheet()
var toPostData = { "name": "John", "email": "fmkfkdf", "message": "", "infoSource": "ddddd" }

// console.log(data.infoSource);
async function putData(data){
    const config = {
        method : 'POST',
        headers : {
            Accept: 'application/json',
            'Content-Type':'application/json',
        },
        body:JSON.stringify(data)
    }
    let resp = await fetch('https://sheet.best/api/sheets/e0955054-83b8-4f7d-a6ec-c919d09f7638',config);
    data = await resp.json()
    document.querySelector("#contactForm").remove()
    document.querySelector(".displayData").classList.toggle("hide")    

}

document.querySelector("#contactForm").onsubmit = (e) => {
    e.preventDefault();
 
    const formData = new FormData(e.target);
    const data = Array.from(formData.entries()).reduce((memo, pair) => ({
        ...memo,
        [pair[0]]: pair[1],
    }), {});

    putData(data);
}

