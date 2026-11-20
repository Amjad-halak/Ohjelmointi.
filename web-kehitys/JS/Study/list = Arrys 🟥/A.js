"use strict";

// 1. تعريف المصفوفة والوصول للعناصر (Arrays)
// ==========================================
// Array = متغير يخزن أكثر من قيمة (يبدأ العد دائماً من الصفر 0)

let fruits = ["banana", "orange", "apple", "dragonfruit"];

console.log(fruits);      // طباعة المصفوفة كاملة
console.log(fruits[0]);   // "banana" (العنصر الأول)
console.log(fruits[3]);   // "dragonfruit" (العنصر الرابع)

// تعديل عنصر موجود:
fruits[0] = "coconut";    // استبدال banana بـ coconut


// 2. الإضافة والحذف (Add & Remove Methods)
// ==========================================
fruits.push("mango");     // إضافة عنصر في النهاية
fruits.pop();             // حذف آخر عنصر

fruits.unshift("peach");  // إضافة عنصر في البداية
fruits.shift();           // حذف أول عنصر

// عرض المصفوفة في الصفحة:
document.getElementById("p1").textContent = fruits.join(", ");


// 3. الطول، البحث، والترتيب (Length, Search & Sort)
// ==========================================
let numOfFruits = fruits.length;        // عدد العناصر (4)
let index = fruits.indexOf("apple");    // مكان العنصر (2)
let notFound = fruits.indexOf("melon"); // يرجع -1 إذا لم يجد العنصر

// إضافة مفيدة: التأكد من وجود العنصر (يرجع true أو false)
let hasApple = fruits.includes("apple"); // true

// الترتيب الأبجدي:
fruits.sort();            // ترتيب من A إلى Z
fruits.sort().reverse();  // ترتيب عكسي من Z إلى A


// 4. التكرار على المصفوفة (Loops in Arrays)
// ==========================================
let cars = ["bmw", "byd", "mazda", "volkswagen"];

// أ) الطريقة المختصرة والأسهل لقراءة العناصر (for...of):
for (let car of cars) {
    console.log(car);
}

// ب) الطريقة التقليدية بالعداد (for loop) من البداية للنهاية:
for (let i = 0; i < cars.length; i++) {
    console.log(cars[i]);
}
document.getElementById("p2").textContent = cars.join(", ");

// ج) الطباعة بالعكس (Reverse Loop) من النهاية للبداية:
let reversedCars = [];
for (let i = cars.length - 1; i >= 0; i--) {
    console.log(cars[i]);
    reversedCars.push(cars[i]); // نجمعها أولاً حتى لا تظهر فاصلة زائدة في النهاية
}
document.getElementById("p3").textContent = reversedCars.join(", ");