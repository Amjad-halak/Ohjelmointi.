"use strict";

// ==========================================
// 1. جلب عناصر الصفحة (DOM Elements)
// ==========================================
const decreaseBtn = document.getElementById("decreaseBtn");
const resetBtn    = document.getElementById("resetBtn");
const increaseBtn = document.getElementById("increaseBtn");
const countLabel  = document.getElementById("countlabel");

// المتغير الأساسي للعدّاد (نستخدم let لأن قيمته ستتغير)
let count = 0;


// 2. برمجة الأزرار (Button Events)
// ==========================================

// زر الزيادة (+1):
increaseBtn.onclick = function () {
    count++;
    countLabel.textContent = count;
};

// زر النقصان (-1):
decreaseBtn.onclick = function () {
    count--;
    countLabel.textContent = count;
};

// زر التصفير (0):
resetBtn.onclick = function () {
    count = 0;
    countLabel.textContent = count;
};