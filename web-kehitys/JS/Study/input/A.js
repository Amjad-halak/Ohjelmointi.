// basic way 
// let username = window.prompt("Who are u ");
// console.log(username);

document.getElementById("mysubmit").onclick = function(){
    username = document.getElementById("mytext").value;
    document.getElementById("myh1").textContent= `hello ${username}`
    
}
