// let pi = 3.14123; ; 
// let radius ; 
// let circumfernece ; 

// pi = 420.69
// radius= window.prompt("enter the radius of a circle : ")
// radius = Number (radius)

// circumfernece = 2 * pi * radius

// console.log(circumfernece)

// document.getElementById("r").textContent = `the circumfernece of ${radius} radius is ${circumfernece} `


const PI = 3.14123; ; 
let radius ; 
let circumfernece ;  

// PI = 420.69         مافيك تعدلها هون بيعطي eror 


document.getElementById("mysubmit").onclick = function(){
    radius=  document.getElementById("mytext").value;
    radius = Number(radius);
    circumfernece = 2 * PI * radius;
    document.getElementById("myh3").textContent = circumfernece;
}