// anna listan keskiarvo functiolla :
// sun ratkaisu 
z= []
function listan_keskiarvo(num){
    z.push(num);
    for (let i of z){
         arvo += i
         const keskiarvo = arvo /z.length
    }
    return
}


// oikeia  ratkaisu 

function listan_keskiarvo(lista) {
  let summa = 0; // 1. نبدأ المجموع من الصفر

  for (const luku of lista) { // 2. نمر على كل رقم داخل المصفوفة (of وليس in)
    summa += luku;
  }

  const keskiarvo = summa / lista.length; // 3. نحسب المتوسط بعد انتهاء الحلقة
  return keskiarvo; // 4. نرجّع النتيجة
}

// طريقة الاستدعاء والاختبار (السؤال بيكون عاطيك مصفوفة جاهزة مثل هي):
const numerot = [10, 20, 30];
console.log(listan_keskiarvo(numerot)); // يطبع: 20


// fetch esimerki 
// sun ratkaisu 
async function random_name(){
    try{
        
    const response = await fetch(
      "https://testaus.com/users/id(هوو قلي احطه هون بلمساله )"
    );
    
    if (!response.ok) {
      return new Error("Eror");
    }}
    
    catch(eror) {
        console.error("Fetch failed:", error.message);
    }

}


// oikeia ratkaisu 
async function haeKayttaja(id) {
  try {
    // 1. إرسال الطلب مع دمج المتغير بالرابط باستخدام `` و ${}
    const response = await fetch(`https://testaus.com/users/${id}`);

    // 2. فحص إذا السيرفر رجّع خطأ (مثل 404)
    if (!response.ok) {
      throw new Error("Verkkovirhe: " + response.status);
    }

    // 3. تحويل الرد إلى بيانات JSON مقروءة (هذا السطر اللي كان ناقصك!)
    const data = await response.json();

    // 4. استخدام البيانات (مثلاً طباعتها أو عرضها بالصفحة)
    console.log(data);
    // أو مثلاً: document.querySelector("#tulos").textContent = data.name;

  } catch (error) {
    // 5. اصطياد أي خطأ وعرضه
    console.error("Fetch failed:", error.message);
  }
}