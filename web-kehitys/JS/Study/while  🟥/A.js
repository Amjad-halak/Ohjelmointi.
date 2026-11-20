// 1. حلقة while (تستمر طالما الشرط صحيح - ممتازة للتحقق من إدخال المستخدم):
let username = "";
while (username === "" || username === null) {
    username = window.prompt("Enter your name:");
}

// 2. التحكم داخل الحلقات (break & continue):
for (let i = 1; i <= 5; i++) {
    if (i === 3) continue; // يتخطى رقم 3 فقط ويكمل الحلقة
    if (i === 5) break;    // يوقف الحلقة تماماً ويخرج منها
    console.log(i);        // يطبع: 1, 2, 4
}