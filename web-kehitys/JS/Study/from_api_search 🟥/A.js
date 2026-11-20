"use strict";

// 1. إمساك عناصر الصفحة
const form = document.querySelector("#search-form");
const query = document.querySelector("#query");
const status = document.querySelector("#status");

// 2. ربط حدث الإرسال بدالة غير متزامنة (async)
form.addEventListener("submit", async function (event) {
  event.preventDefault(); // ⛔ منع تحديث الصفحة

  // إخبار المستخدم أن البحث بدأ (تحديث فوري للواجهة)
  status.innerText = "Loading...";

  try {
    // 3. دمج ما كتبه المستخدم (query.value) داخل رابط الـ API باستخدام Backticks ` `
    const response = await fetch(
      `https://api.tvmaze.com/search/people?q=${query.value}`
    );

    // 4. فحص نجاح الاتصال بالسيرفر
    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }

    // 5. تحويل النتيجة لمصفوفة كائنات JS
    const data = await response.json();

    console.log(data);
    // 6. عرض عدد النتائج للمستخدم في الصفحة
    status.innerText = `Found ${data.length} results. Check the console.`;

  } catch (error) {
    // 7. في حال انقطاع الإنترنت أو فشل الطلب
    console.error(error);
    status.innerText = "Search failed.";
  }
});