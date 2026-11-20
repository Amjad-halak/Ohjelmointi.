"use strict";

// 1. كائن جافاسكريبت عادي (JavaScript Object)
const student = {
  name: "Joa",
  age: 21,
  courses: ["Python", "Webdev"]
};

console.log("JavaScript object:");
console.log(student);

// 2. JSON.stringify: تحويل كائن JS إلى نص (String) لإرساله عبر الإنترنت (للسيرفر)
// (السيرفر لا يفهم كائنات JS مباشرة، يفهم نصوصاً فقط)
const jsonText = JSON.stringify(student);

console.log("JSON text:");
console.log(jsonText);

// 3. JSON.parse: العكس! تحويل النص القادم من السيرفر إلى كائن JS لنستطيع قراءته
const parsedStudent = JSON.parse(jsonText);

console.log("Parsed back to JavaScript:");
console.log(parsedStudent);
console.log(parsedStudent.name); // الآن نقدر نكتب .name ونقرأ الاسم