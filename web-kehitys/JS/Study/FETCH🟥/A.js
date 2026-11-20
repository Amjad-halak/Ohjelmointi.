// الطريقة 1: Async / Await (الطريقة الحديثة والأهم للامتحان)
// ========================================================
"use strict";

async function fetchShow() {
  console.log("Starting fetch.");

  try {
    // 1. إرسال طلب GET وانتظار الرد
    const response = await fetch(
      "https://api.tvmaze.com/singlesearch/shows?q=emmerdale"
    );

    // 2. فحص هل السيرفر رد بنجاح أم أعطى خطأ (مثل 404)
    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }

    // 3. تحويل الرد القادم إلى كائن JS وانتظار اكتمال التحويل
    const data = await response.json();

    console.log("Fetched data:");
    console.log(data);
    console.log("Show name:", data.name); // قراءة اسم المسلسل من الكائن
  } catch (error) {
    // 4. صيد أي خطأ (في الشبكة أو من throw new Error)
    console.error("Fetch failed:", error.message);
  } finally {
    // 5. اختياري: ينفذ دائماً في النهاية سواء نجح الطلب أو فشل
    console.log("Fetch finished.");
  }
}

console.log("Before function call.");
fetchShow();
console.log("After function call.");



// الطريقة 2: .then() / .catch() (الطريقة القديمة - للقراءة والفهم)
// ========================================================
"use strict";

console.log("Before fetch.");

// 1. استدعاء fetch بدون await (تُرجع Promise)
fetch("https://api.tvmaze.com/singlesearch/shows?q=emmerdale")
  // 2. .then الأولى: تستقبل response عندما يصل
  .then(function (response) {
    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }
    return response.json(); // تُرجع Promise جديد للـ .then التالية
  })
  // 3. .then الثانية: تستقبل data الجاهزة
  .then(function (data) {
    console.log("Fetched data:");
    console.log(data);
    console.log("Show name:", data.name);
  })
  // 4. .catch: بديل عن catch في try/catch لصيد الأخطاء
  .catch(function (error) {
    console.error("Fetch failed:", error.message);
  });

console.log("After fetch.");