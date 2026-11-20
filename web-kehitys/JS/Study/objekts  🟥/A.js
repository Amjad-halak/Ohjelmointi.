"use strict";

// 1. الكائن البسيط (Basic Object: Key & Value)
// ==========================================
// Object = مجموعة من الخصائص (key: value) والدوال (Methods) تصف شيئاً واحداً

const human = {
    name: "abuali",
    weight: "723 kg",   // يجب أن يكون نصاً كاملاً بين علامتي تنصيص (أو رقماً فقط 723)
    work: "unemployed"
};

// قراءة الخصائص باستخدام النقطة (Dot Notation):
console.log(human.name);    // "abuali"
console.log(human.weight);  // "723 kg"


// 2. كائن مع دوال وكلمة this (Object with Methods & this)
// ==========================================
const person = {
    firstName: "amjad",
    lastName: "alhalak",
    age: 23,
    height: "185 cm",
    isEmployed: true,
    bestFood: "patty",

    // الطريقة المختصرة لكتابة دالة داخل Object (الأحدث والأفضل):
    sayHello() {
        // كلمة (this) تشير إلى الكائن الحالي نفسه (person)
        console.log(`Hi, I'm ${this.firstName}`);
    },

    sayGoodbye() {
        console.log(`See you soon ${this.lastName}`);
    },

    // الطريقة التقليدية لكتابة دالة داخل Object (كلاهما صحيح):
    eat: function () {
        // تصحيح: نستخدم this.bestFood وليس this.food
        console.log(`I love to eat ${this.bestFood}`);
    }
};

// استدعاء الدوال (Methods) الموجودة داخل الكائن:
person.sayHello();    // Hi, I'm amjad
person.sayGoodbye();  // See you soon alhalak
person.eat();         // I love to eat patty


const car = { brand: "Toyota", model: "Camry" };

car.model = "Corolla"; // 1. تعديل قيمة خاصية موجودة
car.year = 2024;       // 2. إضافة خاصية جديدة للكائن
delete car.brand;      // 3. حذف خاصية من الكائن