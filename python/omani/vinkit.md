# 🐍 PYTHON-MUISTIO & TIETORAKENTEET

---

## 1. Laskutoimitukset (Laskutoimitukset)

| Operaattori | Suomi | Arabic | Kuvaus / Esimerkki |
| :--- | :--- | :--- | :--- |
| `+` | yhteenlasku | الجمع | `5 + 3 = 8` |
| `-` | vähennyslasku | الطرح | `5 - 3 = 2` |
| `*` | kertolasku | الضرب | `5 * 3 = 15` |
| `/` | jakolasku | القسمة | `5 / 2 = 2.5` |
| `**` | potenssiinkorotus | الأس | `2 ** 3 = 8` |
| `//` | kokonaisosan palauttava jakolasku | قسمة صحيحة | `5 // 2 = 2` |
| `%` | jakojäännös | باقي القسمة | `5 % 2 = 1` |

---

## 2. Lukujen ja tekstin muotoilu (Muotoilu)

| Koodi | Suomi | Arabic | Kuvaus |
| :--- | :--- | :--- | :--- |
| `:.5f` | liukuluku, 5 desimaalia | رقم عشري مع 5 أرقام بعد الفاصلة | Pyöristää 5 desimaaliin |
| `:10.2f` | 2 desimaalia, leveys 10 | رقم عشري بعرض 10 خانات | Varaa 10 merkkiä, 2 desimaalia |
| `:<20s` | teksti, leveys 20, vasemmalle | نص بعرض 20 ومحاذاة لليسار | Tasataan vasemmalle |
| `:8d` | kokonaisluku, leveys 8 | عدد صحيح بعرض 8 خانات | Varaa 8 merkkiä luvulle |

---

## 3. Vertailuoperaattorit (Vertailu)

| Operaattori | Suomi | Arabic | Kuvaus |
| :--- | :--- | :--- | :--- |
| `>` | suurempi kuin | أكبر من | `a > b` |
| `<` | pienempi kuin | أصغر من | `a < b` |
| `>=` | suurempi tai yhtä suuri kuin | أكبر من أو يساوي | `a >= b` |
| `<=` | pienempi tai yhtä suuri kuin | أصغر من أو يساوي | `a <= b` |
| `==` | yhtä suuri kuin | يساوي | `a == b` |
| `!=` | eri suuri kuin | لا يساوي | `a != b` |

---

## 4. Loogiset operaattorit (Loogiset operaattorit)

| Operaattori | Kuvaus / Suomi | Arabic | Toiminta |
| :--- | :--- | :--- | :--- |
| `and` | ja | و | Määrittelee, että molempien ehtojen tulee olla tosia. |
| `or` | tai | أو | Riittää, että ainakin toinen ehto on tosi. |
| `not` | ei (kääntää tuloksen) | ليس | Kääntää `True` -> `False` ja päinvastoin. |

---

## 5. Toistorakenteet ja ohjaus (Silmukat)

| Komento | Suomi | Arabic | Kuvaus |
| :--- | :--- | :--- | :--- |
| `while True` | ikuisen silmukan aloitus | بدء حلقة تكرار غير محدودة | Jatkuu kunnes `break`-komento suoritetaan. |
| `break` | keskeyttää silmukan | إيقاف الحلقة والخروج فوراً | Lopettaa silmukan suorituksen välittömästi. |
| `continue` | hyppää seuraavaan kierrokseen | التجاوز للبدء في الدورة التالية | Siirtyy suoraan seuraavaan silmukan kierrokseen. |
| `range(a, b)` | lukusarja a:sta b-1:een | سلسلة أرقام من a إلى قبل b | Luo lukujonon välillä `a` – `b-1`. |

---

## 6. Funktiot luvuille ja listoille (Perusfunktiot)

| Funktio | Suomi | Arabic | Kuvaus |
| :--- | :--- | :--- | :--- |
| `min()` | palauttaa pienimmän arvon | إيجاد أصغر قيمة | Etsii pienimmän alkion. |
| `max()` | palauttaa suurimman arvon | إيجاد أكبر قيمة | Etsii suurimman alkion. |
| `len()` | palauttaa pituuden / määrän | معرفة طول القائمة أو النص | Laskee alkioiden tai merkkien määrän. |
| `sum()` | laskee alkioiden summan | جمع كافة الأرقام | Laskee kaikkien listan lujen summan. |

---

## 7. Listaoperaatiot (Listamethodit)

| Metodi | Suomi | Arabic | Esimerkki |
| :--- | :--- | :--- | :--- |
| `.append()` | lisää alkion loppuun | إضافة عنصر في النهاية | `nimet.append("Matti")` |
| `.remove()` | poistaa alkion | حذف أول عنصر يطابق الاسم | `nimet.remove("Pekka")` |
| `.insert()` | lisää tiettyyn kohtaan | إضافة عنصر في موقع محدد | `nimet.insert(4, "Teppo")` |
| `.extend()` | yhdistää toisen listan | دمج قائمة أخرى | `nimet.extend(["Allu", "Ninni"])` |
| `.index()` | palauttaa alkion indeksin | معرفة رقم موقع العنصر | `monesko = nimet.index("Olga")` |
| `in` | tarkistaa onko alkiota | التحقق من وجود العنصر | `if "Matti" in nimet:` |
| `.sort()` | järjestää listan | ترتيب العناصر تصاعدياً | `luvut.sort()` |
| `.reverse()` | kääntää listan järjestyksen | عكس ترتيب العناصر | `luvut.reverse()` |

---

## 8. Funktiot ja syötteet (Funktio / Parametri / Return)

> 💡 **Kielikuva:** Jääkaappi on funktio (`def`), joka suorittaa jäähdytyksen. Jääkaappiin laitettavat juomat ovat parametreja (`parameters`), ja kylmä juoma on palautusarvo (`return`).

| Käsite / Komento | Suomi | Arabic | Kuvaus |
| :--- | :--- | :--- | :--- |
| `def` | määrittää uuden funktion | تعريف دالة جديدة | `def jaahdyta(juoma):` |
| **parametri** | syöte / muuttuja suluissa | المعامل داخل الأقواس | Odotettu muuttuja funktiorakenteessa |
| **argumentti** | todellinen arvo kutsussa | القيمة الممررة عند التشغيل | Todellinen syötetty arvo kutsussa |
| `return` | palauttaa tuloksen pääohjelmaan | إرجاع النتيجة للبرنامج | Palauttaa tuloksen takaisin muuttujalle |
| `None` | tyhjä paluu / ei return-sanaa | قيمة خالية | Palautetaan, jos `return`-lause puuttuu |
| `pass` | tyhjä komento (varaa paikan) | أمر فارغ لحجز المكان | Varataan paikka tulevalle koodille |
| `*args` | vaihteleva määrä parametreja | عدد غير محدد من المعاملات | Kokoaa parametrit tuple-monikkoon |

---

## 9. Milloin `return` ja milloin `print` luokan sisällä?

Sääntö tentteihin ja oikeaan ohjelmointiin:

### 1. `return`-lauseen käyttö (Kysyvä funktio)
* **Milloin:** Kun funktio laskee, hakee tai tarkistaa arvon (`Get / Calculate / Search`).
* **Syy:** Arvo halutaan tallentaa muuttujaan luokan ulkopuolella tai käyttää toisessa funktiossa.
* **Avainsanat tehtävänannossa:** *Palauttaa* (ترجع), *Laskee ja palauttaa* (تحسب وترجع), *Hae* (احصل على).
* **Esimerkki:**
  ```python
  def hae_tiedot(self):
      return f"Nimi: {self.nimi}"