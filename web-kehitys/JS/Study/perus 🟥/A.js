"use strict";

// 1. أساسيات الطباعة والتنبيهات (Perustieto JS)
// ==========================================

// هذا تعليق برمجي لتوضيح الكود فقط ولا يتم تنفيذه (ympäri koodia)
console.log("this is in console log");
console.log("how to be you!");

window.alert("amjad is gay");


// 2. التعامل مع عناصر الصفحة (DOM Manipulation)
// ==========================================

const tekstiElementti = document.getElementById("teksti");
//       ▲                 ▲            ▲
//    Element            Object       Method

document.getElementById("myh1").textContent = "Hello";
document.getElementById("myp").textContent = "this has been added by js file which connects to html file";


// 3. تحويل أنواع البيانات (Type Conversion)
// ==========================================

// String(): تحويل أي قيمة إلى نص
String(123);   // => "123"

// Number(): تحويل القيمة إلى رقم
Number(45);    // => 45

// Boolean(): تحويل القيمة إلى قيمة منطقية (true أو false)
Boolean(1);    // => true

/*
  ملاحظة: القيم التي تتحول دائماً إلى false (تُسمى Falsy Values) وعددها 6 فقط:
  1. false
  2. 0 (والسالب صفر -0 و 0n)
  3. "" (النص الفارغ بدون مسافات)
  4. null
  5. undefined
  6. NaN
*/


let text = "  Amjad Alhalak  ";

text.length;              // طول النص (عدد الأحرف والمسافات)
text.trim();              // حذف المسافات الزائدة من البداية والنهاية -> "Amjad Alhalak"
text.toUpperCase();       // تحويل لأحرف كبيرة -> "  AMJAD ALHALAK  "
text.toLowerCase();       // تحويل لأحرف صغيرة -> "  amjad alhalak  "
text.startsWith("A");     // هل يبدأ بحرف معين؟ (true / false)
text.endsWith("k");       // هل ينتهي بحرف معين؟ (true / false)
text.replace("a", "o");   // استبدال أول حرف مطابق
text.slice(0, 5);         // قص جزء من النص من البداية للنهاية (مثل المصفوفات)