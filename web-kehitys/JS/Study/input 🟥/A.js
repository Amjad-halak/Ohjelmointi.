"use strict";

// 1. أخذ مدخلات المستخدم (User Input)
// ==========================================

// أ) الطريقة البسيطة (نافذة منبثقة):
// let username = window.prompt("Who are you?");
// console.log(username);

// ب) الطريقة الاحترافية (من حقل إدخال في الصفحة HTML Input):
document.getElementById("mysubmit").onclick = function () {
    let username = document.getElementById("mytext").value;
    document.getElementById("myh1").textContent = `Hello ${username}`;
};


// 2. دوال تحويل النصوص إلى أرقام (String to Number)
// ==========================================
// ملاحظة: دالة prompt() تُرجع النص دائماً كـ String، لذا نحتاج لتحويله إلى رقم:

let age  = parseInt(prompt("Enter your age:"));       // يحوّل إلى عدد صحيح (Integer)
let price = parseFloat(prompt("Enter the price:"));   // يحوّل إلى عدد عشري (Decimal / Float)
let count = Number(prompt("Enter a number:"));        // يحوّل النص بالكامل إلى رقم (صحيح أو عشري)