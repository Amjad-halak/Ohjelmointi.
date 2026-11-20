"use strict";

// 1. دالة بسيطة بدون مدخلات (Basic Function)
// ==========================================
const nimi = window.prompt("Anna nimisi:");

function birthday() {
    document.getElementById("h1").textContent = `Happy birthday to you ${nimi}!`;
}

birthday(); // استدعاء الدالة لتنفيذها


// 2. دالة تستقبل مدخلات (Parameters & Arguments)
// ==========================================
// (name, age) = Parameters (المتغيرات التي تستقبلها الدالة)
function data(name, age) {
    console.log(`Your name is ${name}, and you are ${age} yo.`);
}

// ("rama", 28) = Arguments (القيم الفعلية التي نمررها عند الاستدعاء)
data("rama", 28);
data("spongebob", 21);


// 3. دالة تُرجع قيمة (Return Statement)
// ==========================================
function add(num1, num2) {
    return num1 + num2; // تُرجع الناتج مباشرة وتُنهي الدالة
}

let answer = add(3, 12);
console.log(answer); // 15


// 4. دوال التحقق (Boolean Return Functions)
// ==========================================

// أ) فحص هل الرقم زوجي أم لا (Even / Odd):
const num = Number(window.prompt("Anna kokonaisluku:"));

function isEven(number) {
    // اختصار ذكي: الشرط (number % 2 === 0) يُرجع true أو false أصلاً!
    return number % 2 === 0;
}

const result = isEven(num);
console.log(`${num} is even: ${result}`);


// ب) التحقق من صحة البريد الإلكتروني (Email Validation):
function isValidEmail(email) {
    // دالة includes("@") تُرجع true أو false مباشرة، فلا حاجة لـ if/else
    return email.includes("@");
}

console.log(isValidEmail("al8485359@gmail.com")); // true
console.log(isValidEmail("trump.com"));           // false


function greet(name = "Guest") {
    console.log(`Hello ${name}`);
}
greet();        // "Hello Guest"
greet("Amjad"); // "Hello Amjad"