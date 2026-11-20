"use strict"; // إجبار الجافاسكريبت على العمل بالوضع الصارم (يمنع الأخطاء الصامتة)

/* ==========================================================================
   الجزء 1: الأساسيات (Variables, Conditions, Loops, Arrays, Objects, Functions)
   (تعمل في الـ Console - افتح F12 في المتصفح لرؤيتها)
   ========================================================================== */

// 1. المتغيرات (Variables):
// const = قيمة ثابتة لا تتغير (الأكثر استخداماً)
// let   = قيمة متغيرة (مثل العدادات)
const courseName = "Ohjelmisto 2";
let examAttempts = 1;
examAttempts += 1; // أصبحت 2

// 2. أنواع البيانات وتحويلها (Type Conversion):
const numText = "42";
const realNumber = Number(numText); // تحويل النص إلى رقم (أو parseInt / parseFloat)
const backToText = String(realNumber); // تحويل الرقم إلى نص

// 3. الشروط (If / Else):
const score = 75;
if (score >= 90) {
    console.log("Grade: 5");
} else if (score >= 50) {
    console.log("Passed! (نجاح)");
} else {
    console.log("Failed (رسوب)");
}

// 4. المصفوفات (Arrays) والحلقات (Loops):
const topics = ["Variables", "DOM", "Events", "Fetch", "JSON"];

// حلقة for...of (الأهم والأسهل للمرور على المصفوفات)
for (const topic of topics) {
    console.log("Topic:", topic);
}


// 5. الكائنات (Objects) و JSON:
const student = {
    name: "Student",
    age: 22,
    isReady: true
};
console.log("Student name:", student.name); // الوصول للخاصية بالنقطة

// تحويل الكائن لنص JSON والعكس:
const jsonString = JSON.stringify(student); // Object -> String (للإرسال للسيرفر)
const parsedObj = JSON.parse(jsonString);   // String -> Object (عند الاستلام)

// // 1. كائن جافاسكريبت عادي
// const user = { name: "Sara", age: 21 };

// // 2. stringify: تحويل الكائن إلى نص JSON (للإرسال للسيرفر)
// const text = JSON.stringify(user);   // '{"name":"Sara","age":21}'

// // 3. parse: تحويل نص JSON إلى كائن (للقراءة بالنقطة)
// const obj = JSON.parse(text);        // { name: "Sara", age: 21 }
// console.log(obj.name);               // "Sara"


/* ==========================================================================
   الجزء 2: التفاعل مع الصفحة (DOM + Events) - القسم 1 في HTML
   ========================================================================== */

// إمساك العناصر من HTML عبر ID (#)
const statusText = document.querySelector("#status-text");
const counterDisplay = document.querySelector("#counter-value");
const btnPlus = document.querySelector("#btn-plus");
const btnReset = document.querySelector("#btn-reset");

let count = 0;

function increaseCounter() {
    count++;
    counterDisplay.textContent = count; // تغيير النص داخل العنصر
    statusText.textContent = "تمت زيادة العداد بنجاح!";
}

function resetCounter() {
    count = 0;
    counterDisplay.textContent = count;
    statusText.textContent = "تم تصفير العداد.";
}

// ربط الأحداث بالأزرار (بدون أقواس بعد اسم الدالة!)
btnPlus.addEventListener("click", increaseCounter);
btnReset.addEventListener("click", resetCounter);


/* ==========================================================================
   الجزء 3: بناء قائمة ديناميكية (createElement + appendChild) - القسم 2 في HTML
   ========================================================================== */

const btnLoadList = document.querySelector("#btn-load-list");
const coursesList = document.querySelector("#courses-list");

function renderCourses() {
    coursesList.innerHTML = ""; // تنظيف القائمة أولاً لمنع التكرار

    for (const item of topics) {
        const li = document.createElement("li"); // 1. إنشاء عنصر <li> في الذاكرة
        li.textContent = item;                   // 2. وضع النص بداخله
        coursesList.appendChild(li);             // 3. إلصاقه داخل <ul> في الصفحة
    }
}

btnLoadList.addEventListener("click", renderCourses);


/* ==========================================================================
   الجزء 4: التعامل مع النماذج (Forms + Submit + preventDefault) - القسم 3 في HTML
   ========================================================================== */

const userForm = document.querySelector("#user-form");
const firstNameInput = document.querySelector("#first-name");
const greetingSelect = document.querySelector("#greeting-select");
const formResult = document.querySelector("#form-result");

function handleUserForm(event) {
    event.preventDefault(); // ⛔ أهم سطر: يمنع الصفحة من إعادة التحميل!

    // قراءة القيم من <input> و <select> باستخدام .value
    const nameValue = firstNameInput.value;
    const greetingValue = greetingSelect.value;

    formResult.textContent = `${greetingValue}, ${nameValue}! أهلاً بك في الامتحان.`;
}

userForm.addEventListener("submit", handleUserForm);


/* ==========================================================================
   الجزء 5: جلب البيانات من الإنترنت (Async / Await + Fetch GET) - القسم 4 في HTML
   ========================================================================== */

const searchForm = document.querySelector("#search-form");
const searchQuery = document.querySelector("#search-query");
const apiResults = document.querySelector("#api-results");

// لاحظ كلمة async قبل function لأن بداخلها await
async function handleSearch(event) {
    event.preventDefault();
    apiResults.innerHTML = "جاري التحميل...";

    try {
        // 1. إرسال الطلب وانتظار الرد
        const response = await fetch(
            `https://api.tvmaze.com/search/people?q=${searchQuery.value}`
        );

        // 2. التأكد أن السيرفر لم يُرجع خطأ (مثل 404)
        if (!response.ok) {
            throw new Error("HTTP Error: " + response.status);
        }

        // 3. تحويل الرد إلى مصفوفة/كائن JS
        const data = await response.json();
        apiResults.innerHTML = ""; // مسح كلمة جاري التحميل

        // 4. بناء بطاقات HTML لكل نتيجة
        for (const item of data) {
            const person = item.person;

            const article = document.createElement("article");
            const h3 = document.createElement("h3");
            const img = document.createElement("img");

            h3.textContent = person.name;

            // فحص وجود صورة لتجنب خطأ null
            if (person.image !== null) {
                img.src = person.image.medium;
            } else {
                img.src = "https://placehold.co/210x295?text=No+Image";
            }

            article.appendChild(h3);
            article.appendChild(img);
            apiResults.appendChild(article);
        }
    } catch (error) {
        // صيد أي خطأ في الاتصال أو الكود
        console.error(error);
        apiResults.textContent = "حدث خطأ أثناء جلب البيانات.";
    }
}

searchForm.addEventListener("submit", handleSearch);


/* ==========================================================================
   الجزء 6: إرسال بيانات للسيرفر (Fetch POST + JSON.stringify) - القسم 5 في HTML
   ========================================================================== */

const btnSendPost = document.querySelector("#btn-send-post");
const postResult = document.querySelector("#post-result");

async function sendPostData() {
    postResult.textContent = "جاري الإرسال...";

    const payload = {
        student: "Metropolia Student",
        course: "Ohjelmisto 2",
        status: "Ready for Uusintakoe!"
    };

    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
            method: "POST",                                      // تحديد نوع الطلب POST
            headers: {
                "Content-Type": "application/json"               // إخبار السيرفر أن البيانات JSON
            },
            body: JSON.stringify(payload)                        // تحويل الكائن إلى نص JSON
        });

        if (!response.ok) {
            throw new Error("HTTP Error: " + response.status);
        }

        const responseData = await response.json();
        postResult.textContent = JSON.stringify(responseData, null, 2);
    } catch (error) {
        console.error(error);
        postResult.textContent = "فشل الإرسال.";
    }
}

btnSendPost.addEventListener("click", sendPostData);