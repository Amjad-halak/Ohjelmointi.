"use strict";

// 1. جمل الشروط الأساسية (IF / ELSE IF / ELSE)
// ==========================================
// إذا تحقق الشرط (true) ينفذ الكود، وإلا ينتقل للشرط التالي

let time = 9;

if (time < 12) {
    document.getElementById("p2").textContent = "Good morning!";
} 
// تصحيح مهم: في JS لا نكتب (12 < time < 17) بل نربط الشرطين بـ &&
else if (time >= 12 && time < 17) {
    document.getElementById("p2").textContent = "Good afternoon!";
} 
else {
    document.getElementById("p2").textContent = "Good evening!";
}


// 2. التحقق من القيم المنطقية والأرقام (Booleans & ===)
// ==========================================
let isStudent = true;

// بما أن القيمة true أو false أصلاً، لا داعي لكتابة (isStudent === true)
if (isStudent) {
    console.log("You are a student");
} else {
    console.log("You are not a student!");
}

let count = 0;
if (count === 0) {
    console.log("Checked using === and it is true");
}


// 3. مشروع صغير: التحقق من العمر (Age Checker Project)
// ==========================================
const myText = document.getElementById("myText");
const mySubmit = document.getElementById("mySubmit");
const resultElement = document.getElementById("p2");

mySubmit.onclick = function () {
    // تحويل النص المدخل إلى رقم
    let age = Number(myText.value);

    // ملاحظة: الترتيب مهم! نبدأ بالحالات الخاصة (أكبر من 100 أو أصغر من 0) أولاً
    if (age >= 100) {
        resultElement.textContent = "You are TOO OLD to enter this site.";
    } 
    else if (age < 0) {
        resultElement.textContent = "Your age can't be below 0.";
    } 
    else if (age === 0) {
        resultElement.textContent = "You can't enter. You were just born.";
    } 
    else if (age >= 18) {
        resultElement.textContent = "You are old enough to enter this site.";
    } 
    else {
        resultElement.textContent = "You must be 18+ to enter this site.";
    }
};