"use strict";

// 1. إمساك العناصر (تأكدي من تطابق الـ id تماماً)
const countDisplay = document.querySelector("#count");
const nouse = document.querySelector("#nouse_button");
const reset = document.querySelector("#reset_button");

// 2. متغير الرقم (باسم مختلف عن العنصر!)
let count = 0;

// 3. الدوال (تغيّر الرقم ثم تحدّث نص الفقرة countDisplay)
function increase() {
  count++;
  countDisplay.textContent = count;
}

function resetCount() {
  count = 0;
  countDisplay.textContent = count;
}

// 4. ربط الأزرار بالدوال في الأسفل (لاحظي: addEventListener بدون s)
nouse.addEventListener("click", increase);
reset.addEventListener("click", resetCount);