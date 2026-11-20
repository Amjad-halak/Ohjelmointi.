"use strict";



console.log("Program starts.");

setTimeout(function () {
  console.log("This runs after 2 seconds.");
}, 2000);

console.log("Program reaches the end of the script.");


//


async function fetchShow() {
  console.log("Starting fetch.");

  try {
    const response = await fetch(
      "https://api.tvmaze.com/singlesearch/shows?q=emmerdale"
    );

    if (!response.ok) {
      throw new Error("HTTP error! Status: " + response.status);
    }

    const data = await response.json();

    console.log("Fetched data:");
    console.log(data);
    console.log("Show name:", data.name);
  } catch (error) {
    console.error("Fetch failed:", error.message);
  } finally {
    console.log("Fetch finished.");
  }
}

console.log("Before function call.");
fetchShow();
console.log("After function call.");

// ==========================================
// 1. تعريف المهام (كل دالة تُرجع Promise "وعد")
// ==========================================
// الـ Promise هو كائن يمثل عملية تأخذ وقتاً، وله نتيجتان فقط:
// - resolve(قيمة): نجحت المهمة وهذه هي النتيجة.
// - reject(خطأ): فشلت المهمة وهذه هي رسالة الخطأ.

function walkDog() {
    return new Promise((resolve, reject) => {
        setTimeout(() => { // محاكاة مهمة تأخذ 1.5 ثانية
            const dogWalked = true;

            if (dogWalked) {
                resolve("You walk the dog 🐕"); // نجاح ✅
            } else {
                reject("You DIDN'T walk the dog"); // فشل ❌
            }
        }, 1500);
    });
}

function cleanKitchen() {
    return new Promise((resolve, reject) => {
        setTimeout(() => { // محاكاة مهمة تأخذ 2.5 ثانية
            const kitchenCleaned = true;

            if (kitchenCleaned) {
                resolve("You clean the kitchen 🧹"); // نجاح ✅
            } else {
                reject("You DIDN'T clean the kitchen"); // فشل ❌
            }
        }, 2500);
    });
}

function takeOutTrash() {
    return new Promise((resolve, reject) => {
        setTimeout(() => { // محاكاة مهمة تأخذ 0.5 ثانية
            const trashTakenOut = true;

            if (trashTakenOut) {
                resolve("You take out the trash ♻"); // نجاح ✅
            } else {
                reject("You DIDN'T take out the trash"); // فشل ❌
            }
        }, 500);
    });
}


// ==========================================
// 2. تشغيل المهام بالترتيب باستخدام Async / Await
// ==========================================
// كلمة async قبل الدالة: تخبر JS أن بداخل هذه الدالة أوامر انتظار (await)
async function doChores() {

    // try / catch: لصيد الأخطاء إذا تحول أي Promise إلى reject
    try {
        // await: أوقف التنفيذ هنا وانتظر حتى تنتهي walkDog() وتُرجع النتيجة
        const walkDogResult = await walkDog();
        console.log(walkDogResult); // يُطبع بعد 1.5 ثانية

        // لن يبدأ هذا السطر إلا بعد انتهاء المهمة الأولى تماماً
        const cleanKitchenResult = await cleanKitchen();
        console.log(cleanKitchenResult); // يُطبع بعد 2.5 ثانية إضافية

        // لن يبدأ هذا السطر إلا بعد انتهاء المهمة الثانية تماماً
        const takeOutTrashResult = await takeOutTrash();
        console.log(takeOutTrashResult); // يُطبع بعد 0.5 ثانية إضافية

        console.log("You finished all the chores!"); // يُطبع في النهاية
    }
    catch (error) {
        // إذا كانت إحدى المتغيرات false (فشل الوعد)، يقفز الكود فوراً إلى هنا
        console.error(error);
    }
}

// استدعاء الدالة لبدء التنفيذ
doChores();



async function getData() {
    try {
        const response = await fetch("URL"); // 1. جلب الرد (تحتاج await)
        const data = await response.json();  // 2. تحويل الرد لكائن JS (تحتاج await)
        console.log(data);                   // 3. عرض البيانات
    } catch (error) {
        console.error(error);                // 4. صيد الخطأ
    }
}