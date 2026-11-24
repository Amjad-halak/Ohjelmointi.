// Avaa kansio t2 kehitysympäristössäsi tai editorissasi. Lisää HTML-koodia metodien createElement() ja appendChild() avulla. (2p)
// Lisää seuraava HTML-koodi elementtiin, jolla on id="target":
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
// Lisää luettelon toiselle <li>-elementille luokka my-item.
"use strict"
const targetElement = document.getElementById("target")

const li1 = document.createElement(`li`)
li1.textContent = "First item"
targetElement.appendChild(li1)

const li2 = document.createElement(`li`)
li2.textContent = "Second item"
targetElement.appendChild(li2)

const li3 = document.createElement(`li`)
li3.textContent = "Third item"
targetElement.appendChild(li3)

li2.classList.add("my-item")