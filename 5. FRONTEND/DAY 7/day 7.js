// 1. Write a JavaScript program to list the properties of a JavaScript object.Sample object: var student = { name: "David Rayy", sclass: "VI", rollno: 12 }; Sample Output: name, sclass, rollno
var student = { name: "David Rayy", sclass: "VI", rollno: 12 };
const fetchProperties = function(objectx) 
{
    var ans = "";
    for(let x in objectx){
        ans += x+",";
    }
    return ans.slice(0,-1);
}
// console.log(fetchProperties(student));

//--------------------------------------------------------------


// 2. Write a JavaScript program to delete the rollno property from the following object.Also print the object before or after deleting the property.Sample object: var student = { name: "David Rayy", sclass: "VI", rollno: 12 };
console.log(student);
delete student.rollno;
console.log(student);

//--------------------------------------------------------------

// 3. Write a JavaScript program to get the length of a JavaScript object.Sample object: var student = { name: "David Rayy", sclass: "VI", rollno: 12 };

const lenOfObject = function (objectx) {
    c = 0;
    for(let x in objectx){
        c++;
    }
    return c;
}

// console.log(lenOfObject(student));

//--------------------------------------------------------------

// 4. Write a JavaScript program to display the reading status(i.e.display book name, author name and reading status) of the following books.var library = [{ author: 'Bill Gates', title: 'The Road Ahead', readingStatus: true }, { author: 'Steve Jobs', title: 'Walter Isaacson', readingStatus: true }, { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', readingStatus: false }];

var library = [{ author: 'Bill Gates', title: 'The Road Ahead', readingStatus: true }, { author: 'Steve Jobs', title: 'Walter Isaacson', readingStatus: true }, { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', readingStatus: false }];

const printDataFromObj = function(objectx){
    for(let obj in objectx){
        console.log("Current Book :", objectx[obj].title, "\nAuthor's Name :", objectx[obj].author, "\nReading Status :", objectx[obj].readingStatus,"\n");
    }
}
// console.log(printDataFromObj(library))


//--------------------------------------------------------------

// 5. Write a JavaScript program to get the volume of a Cylinder with four decimal places using object classes.Volume of a cylinder: V = πr2h where r is the radius and h is the height of the cylinder.Try To Attempt: Difficult Level Increased

var cylinder = new Object;
cylinder["r"] = prompt("Enter radius for cylinder", 0.00);
cylinder["h"] = prompt("Enter height for cylinder", 0.00);
alert((2*(22/7)*cylinder.r*cylinder.h).toFixed(4));

//--------------------------------------------------------------

// 6. Write a JavaScript program to sort an array of JavaScript objects.Sample Object: var library = [{ title: 'The Road Ahead', author: 'Bill Gates', libraryID: 1254 }, { title: 'Walter Isaacson', author: 'Steve Jobs', libraryID: 4264 }, { title: 'Mockingjay: The Final Book of The Hunger Games', author: 'Suzanne Collins', libraryID: 3245 }]; Expected Output: [[object Object] { author: "Walter Isaacson", libraryID: 4264, title: "Steve Jobs" }, [object Object] { author: "Suzanne Collins", libraryID: 3245, title: "Mockingjay: The Final Book of The Hunger Games" }, [object Object] { author: "The Road Ahead", libraryID: 1254, title: "Bill Gates" }]

var library = [{ title: 'The Road Ahead', author: 'Bill Gates', libraryID: 1254 }, { title: 'Walter Isaacson', author: 'Steve Jobs', libraryID: 4264 }, { title: 'Mockingjay: The Final Book of The Hunger Games', author: 'Suzanne Collins', libraryID: 3245 }];

// [[object Object] 
// { author: "Walter Isaacson", libraryID: 4264, title: "Steve Jobs" },
//  [object Object] { author: "Suzanne Collins", libraryID: 3245, title: "Mockingjay: The Final Book of The Hunger Games" }, 
//  [object Object] { author: "The Road Ahead", libraryID: 1254, title: "Bill Gates" }]
const sortedObj = function(objectx){
    var retArray = new Array();
    for(let obj in objectx){
        retObj = new Object();
        objList = []
        for(let x in objectx[obj]){
            objList.push(x);
        }
        objList = objList.sort();
        for(let m in objList){
            retObj[objList[m]] = objectx[obj][objList[m]];
        }
        retArray.push(retObj);
    }
    return retArray;
}
console.log(sortedObj(library));
// console.log(library);