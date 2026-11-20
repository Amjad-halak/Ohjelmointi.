"use strict";

// 1. تعريف المتغيرات وإسناد القيم (Declaration & Assignment)
// ==========================================
// 1. Declaration (التصريح / حجز مكان): let x;
// 2. Assignment  (الإسناد / إعطاء قيمة): x = 100;

let x = 141;          // عدد صحيح (Number - Integer)
let price = 10.99;    // عدد عشري (Number - Float)
let age = 25;

console.log(x);
console.log(price);


// 2. النصوص الذكية Template Literals (``)
// ==========================================
// نستخدم علامة الـ Backtick (` `) بدلاً من (" ") لدمج المتغيرات بسهولة باستخدام ${}
const firstName = "Amjad";
let email = "al8485359@gmail.com";
let isStudent = true;

console.log(`Average age in his channel is ${age} and price is ${price}`);
console.log(`My first name is ${firstName}`);
console.log(`Email is ${email}`);
console.log(`Enrolled as student: ${isStudent}`);


// 3. فحص نوع البيانات (typeof)
// ==========================================
console.log(typeof age);        // "number"
console.log(typeof firstName);  // "string"
console.log(typeof isStudent);  // "boolean"


// 4. عرض البيانات في صفحة HTML (DOM Output)
// ==========================================
let fullName = "Amjad Alhalak";
let ika = 23;
let student = true;

document.getElementById("num1").textContent = `Random number ${x}`;
document.getElementById("p1").textContent = `Human's full name is ${fullName}`;
document.getElementById("p2").textContent = `And his age is ${ika}`;
document.getElementById("p3").textContent = `Is he/she a student: ${student}`;