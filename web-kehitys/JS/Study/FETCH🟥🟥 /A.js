// fetch = Function used for making HTTP requests to fetch resources.
//         (JSON style data, images, files)
//         Simplifies asynchronous data fetching in JavaScript and
//         used for interacting with APIs to retrieve and send
//         data asynchronously over the web.
//         fetch(url, {options})


// 1. the normal fetch 
// fetch(`https://pokeapi.co/api/v2/pokemon/pikachu`)
//   .then(function (response) { console.log(response); })
//   .catch(function (error) { console.error(error); });


// 2. adding json to it 
// fetch(`https://pokeapi.co/api/v2/pokemon/pikachu`)
//   .then(function (response) {
//     return response.json();
//   })
//   .then(function (data) { console.log(data.weight), console.log(data.name), console.log(data.age); }) // data.name / data.id انو فيك تطبع اي معلومة من ال url
//   .catch(function (error) { console.error(error); });


// 3. .then + using if statement in fetch 
// fetch(`https://pokeapi.co/api/v2/pokemon/pikachu`)
//   .then(function (response) {
//     if (!response.ok) {
//       throw new Error("Could not fetch :) ");
//     }
//     else { return response.json(); }
//   })
//   .then(function (data) { console.log(data.weight), console.log(data.name), console.log(data.age), console.log(data); }) // data.name / data.id انو فيك تطبع اي معلومة من ال url
//   .catch(function (error) { console.error(error); });


// 4. using await and async in function 
// no parameters 
// async function FetchData() {
//   try {
//     const response = await fetch(`https://pokeapi.co/api/v2/pokemon/pikachu`);
//     if (!response.ok) {
//       throw new Error("iha randomi error fuck u !");
//     }
//     else {
//       const data = await response.json();
//       console.log(data);
//     }
//   }
//   catch (error) {
//     console.error(error);
//   }
// }
// FetchData();


// 5. projekti using HTML and DOM
async function FetchData() {
  try {
    const pokemonName = document.getElementById("pokemonName").value.toLowerCase();
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
    if (!response.ok) {
      throw new Error("it fuck up!");
    }
    else {
      const data = await response.json();
      const pokemonPhoto = data.sprites.front_default;
      const imgElement = document.getElementById("pokemonPhoto");

      imgElement.src = pokemonPhoto;
      imgElement.style.display = "block";
    }
  }
  catch (error) {
    console.error(error);
  }
}

const btn = document.getElementById("btn");
btn.addEventListener("click", FetchData);


// ==========================================
// القوالب العامة للمراجعة (Templates)
// ==========================================

// الشكل القديم (.then / .catch)
// function FetchData() {
//   fetch("url")
//     .then(function (response) {
//       if (!response.ok) {
//         throw new Error("أي شي فيك تكتب");
//       }
//       else {
//         return response.json(); // هون نرجّع النتيجة للـ then اللي بعدها
//       }
//     })
//     .then(function (data) {
//       console.log(data); // هون نستلم البيانات جاهزة
//     })
//     .catch(function (error) {
//       console.error(error); // هون نلقط أي خطأ صار فوق
//     });
// }


// الشكل الجديد (async / await + try / catch)
// async function FetchData() {
//   try {
//     const response = await fetch("url");
//     if (!response.ok) {
//       throw new Error("أي شي فيك تكتب");
//     }
//     else {
//       const data = await response.json(); // هون نستنى فك التشفير ونخزنه بمتغير
//       console.log(data); // هون نستخدم البيانات جاهزة
//     }
//   }
//   catch (error) {
//     console.error(error); // هون نلقط أي خطأ صار جوا try
//   }
// }