"use strict";

// 1. الثوابت والمتغيرات (Constants & Variables)
// ==========================================
// const = قيمة ثابتة لا يمكن تغييرها لاحقاً (ويُفضل كتابة اسمها بأحرف كبيرة مثل PI)
const PI = 3.14159; 
let radius;
let circumference;

// PI = 420.69; // ❌ خطأ (TypeError): لا يمكن تعديل قيمة متغير معرّف بـ const


// 2. الطريقة الأولى: الإدخال عبر نافذة منبثقة (Window Prompt)
// ==========================================
/*
radius = Number(window.prompt("Enter the radius of a circle:"));
circumference = 2 * PI * radius;

console.log(circumference);
document.getElementById("r").textContent = `The circumference of ${radius} radius is ${circumference}`;
*/


// 3. الطريقة الثانية (الأفضل): الإدخال عبر حقل في الصفحة (HTML Input)
// ==========================================
document.getElementById("mysubmit").onclick = function () {
    // 1. قراءة القيمة من مربع النص وتحويلها إلى رقم
    radius = Number(document.getElementById("mytext").value);

    // 2. حساب محيط الدائرة (2 × π × نق)
    circumference = 2 * PI * radius;

    // 3. عرض النتيجة في الصفحة
    document.getElementById("myh3").textContent = `${circumference} cm`;
};