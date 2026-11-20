"use strict";

// 1. مشكلة عدم التحويل (String Concatenation)
// ==========================================
// دالة prompt() ترجع النص دائماً كـ String، لذا علامة (+) تقوم بدمج النصوص بدل الجمع:
/*
let age = window.prompt("How old are you:"); // لو أدخل المستخدم "23"
age += 1;                                    // "23" + 1 = "231" (دمج نصي!)
console.log(age);                            // "231"
console.log(typeof age);                     // "string"
*/


// 2. الحل: التحويل إلى رقم قبل الحساب (Type Conversion)
// ==========================================
let age = window.prompt("How old are you:");

age = parseInt(age);   // يحوّل إلى عدد صحيح (Integer)
// age = Number(age);     // يحوّل إلى رقم كامل (صحيح أو عشري)
// age = parseFloat(age); // يحوّل إلى عدد عشري (Float)

age += 1;                // 23 + 1 = 24 (جمع حسابي صحيح!)
console.log(age);        // 24
console.log(typeof age); // "number"


// 3. حالات خاصة عند التحويل (NaN & Boolean)
// ==========================================

// أ) محاولة تحويل نص غير رقمي إلى رقم:
let x = "pizza";
x = Number(x);
console.log(x, typeof x); // NaN "number" (NaN تعني Not a Number، لكن نوعها البرمجي يبقى number!)

// ب) تحويل النص إلى قيمة منطقية (Boolean):
let y = "pizza";
y = Boolean(y);           // تصحيح: حوّلنا y وليس x
console.log(y, typeof y); // true "boolean" (أي نص غير فارغ يعطي true)