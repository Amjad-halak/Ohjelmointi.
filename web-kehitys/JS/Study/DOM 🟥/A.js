"use strict";

// 1. ما هو الـ DOM؟ (Document Object Model)
// ==========================================
// كائن (Object) يمثل صفحة الويب كشجرة عناصر، ويسمح لـ JS بتعديل المحتوى والهيكل والتصميم.
console.log(document);  // يعرض كود HTML الخاص بالصفحة
console.dir(document);  // يعرض كل خصائص ودوال كائن document بالتفصيل


// 2. تعديل خصائص الصفحة العامة (Title & Style)
// ==========================================
document.title = "My Website";
document.body.style.backgroundColor = "hsl(0, 100%, 98%)"; // لون خلفية وردي فاتح جداً


// 3. الوصول للعناصر وتعديل النصوص (Selecting & Modifying Text)
// ==========================================
const username = "Amjad";
const welcomeMsg = document.getElementById("welcome-msg");

// استخدام المعامل الثلاثي (? :) لإضافة الاسم أو "Guest"
welcomeMsg.textContent += username === "" ? "Guest" : username;

// استخدام querySelector (يدعم # للـ ID و . للـ Class)
const title = document.querySelector("#myh1");
const btn = document.querySelector(".myBtn");


// 4. إنشاء العناصر وإضافتها للصفحة (Creating & Appending Elements)
// ==========================================
const body = document.body;

// إنشاء عنصر <div> جديد وإضافته للصفحة
const div = document.createElement("div");
body.append(div);

// الفرق المهم بين textContent و innerHTML:
// div.textContent = "<strong>Hello World</strong>"; // ❌ يطبع الوسوم كنص عادي حرفياً
div.innerHTML = "<strong>Hello World</strong>";      // ✅ يفهم الوسم ويجعل الخط عريضاً (Bold)


// 5. حذف ونقل العناصر (Removing & Moving Elements)
// ==========================================
const spanHi = document.querySelector("#hi");
const spanBey = document.querySelector("#bey");

spanBey.remove();       // حذف العنصر من مكانه الأصلي داخل #message
div.append(spanBey);    // إعادة لصقه داخل الـ div الجديد الذي أنشأناه


// 6. التعامل مع الخصائص والبيانات (Attributes & Dataset)
// ==========================================
spanBey.id = "bey1";                                  // تغيير الـ ID مباشرة
console.log("ID:", spanHi.id);                        // قراءة الـ ID
console.log("Title:", spanHi.title);                  // قراءة الـ Title
console.log("Get Attr:", spanBey.getAttribute("id")); // قراءة أي خاصية بالاسم

// ملاحظة: setAttribute تغيّر القيمة فقط ولا تُرجع شيئاً (لذلك لا نضعها داخل console.log)
spanBey.setAttribute("title", "New tooltip text");
spanBey.removeAttribute("id");                        // حذف خاصية الـ ID

// قراءة خصائص data-* المخزنة في HTML
console.log("Dataset:", spanHi.dataset);
console.log("Test data:", spanHi.dataset.test);


// 7. التحكم بالكلاسات والتصميم (Classes & CSS Styles)
// ==========================================
spanHi.classList.add("active");      // إضافة كلاس
spanHi.classList.remove("hi");       // حذف كلاس
spanHi.classList.toggle("highlight"); // تبديل الكلاس (يضيفه إن لم يكن موجوداً، ويحذفه إن وجد)

spanHi.style.backgroundColor = "red";
spanHi.style.color = "white";
spanBey.style.backgroundColor = "green";
spanBey.style.color = "white";