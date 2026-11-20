"use strict";

// eventListener = Listen for specific events to create interactive web pages
//                 .addEventListener(event, callback);

const myBox = document.getElementById("myBox");

// ==========================================
// 1. تعريف الدوال (Callback Functions)
// ==========================================

// 1. كبسة واحدة (Click)
function handleClick(event) {
    event.target.style.backgroundColor = "red";
    event.target.textContent = "OUCH! 🤕";
    console.log("click");
}

// 2. كبستين بسرعة (Double Click)
function handleDoubleClick(event) {
    event.target.style.backgroundColor = "purple";
    event.target.style.color = "white";
    event.target.textContent = "DOUBLE OUCH! 🤯";
    console.log("dblclick");
}

// 3. لحظة الضغط المستمر على زر الماوس (Mouse Down)
function handleMouseDown(event) {
    event.target.style.backgroundColor = "darkred";
    event.target.textContent = "Holding down... 👇";
    console.log("mousedown");
}

// 4. لحظة إفلات زر الماوس (Mouse Up)
function handleMouseUp(event) {
    event.target.style.backgroundColor = "orange";
    event.target.textContent = "Released! 👆";
    console.log("mouseup");
}

// 5. تحريك الماوس داخل الصندوق (Mouse Move)
function handleMouseMove(event) {
    event.target.textContent = `X: ${event.clientX}, Y: ${event.clientY}`;
    console.log(`mousemove: x=${event.clientX}, y=${event.clientY}`);
}

// 6. دخول الماوس إلى الصندوق أو عناصره الداخلية (Mouse Over)
function handleMouseOver(event) {
    event.target.style.backgroundColor = "yellow";
    event.target.style.color = "black";
    event.target.textContent = "Don't do it 😲";
    console.log("mouseover");
}

// 7. خروج الماوس من الصندوق أو عناصره الداخلية (Mouse Out)
function handleMouseOut(event) {
    event.target.style.backgroundColor = "lightgreen";
    event.target.style.color = "black";
    event.target.textContent = "Click Me 😀";
    console.log("mouseout");
}

// 8. دخول الماوس إلى حدود الصندوق نفسه فقط (Mouse Enter)
function handleMouseEnter(event) {
    event.target.style.border = "4px solid blue";
    console.log("mouseenter");
}

// 9. خروج الماوس من حدود الصندوق نفسه فقط (Mouse Leave)
function handleMouseLeave(event) {
    event.target.style.border = "none";
    console.log("mouseleave");
}

// 10. كبسة زر الماوس اليمين (Right Click / Context Menu)
function handleContextMenu(event) {
    event.preventDefault(); // يمنع ظهور قائمة المتصفح الافتراضية
    event.target.style.backgroundColor = "black";
    event.target.style.color = "white";
    event.target.textContent = "Right Clicked! 🖱️";
    console.log("contextmenu");
}


// ==========================================
// 2. ربط الأحداث بالعنصر (Event Listeners)
// ==========================================

myBox.addEventListener("click", handleClick);
myBox.addEventListener("mouseover", handleMouseOver);
myBox.addEventListener("mouseout", handleMouseOut);


// anothe example 

const btn = document.getElementById("btn");

function handleBtnClick(event) {
    event.target.style.backgroundColor = "gray";
    event.target.textContent = "Don't do it again";
    event.target.style.color = "red";
    console.log("click");
}

btn.addEventListener("click", handleBtnClick);