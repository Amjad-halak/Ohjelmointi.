"use strict";

// 1. إمساك القائمة الفارغة من HTML
const list = document.querySelector("#my_list");

// 2. المصفوفة التي نريد عرض عناصرها
const items = ["Apple", "Banana", "Orange"];

// 3. المرور على كل عنصر في المصفوفة وبناء <li> له
for (const item of items) {
  const li = document.createElement("li"); // أ) إنشاء عنصر <li> جديد
  li.textContent = item;                   // ب) وضع النص بداخله
  list.appendChild(li);                    // ج) إلصاقه داخل <ul> في الصفحة
}