#teht.5  (koitaka muodusta uuden tapa laskea leiviskät, naulat ja luodit grammoiksi)

leiviskät = float(input("Anna leiviskät.\n"))   #leiviksi-lkm
naulat = float(input("Anna naulat.\n"))         #naulat-lkm
luodit = float(input("Anna luodit.\n"))         


#. \n  Pythonissa rivinvaihtoa eli uuden rivin aloittamista.

yhteensa_luodit = (leiviskät * 20 * 32) + (naulat * 32) + luodit
yhteensa_grammat = yhteensa_luodit * 13.3
kilogrammat = int(yhteensa_grammat // 1000)
grammat = yhteensa_grammat % 1000


#toinen tapa laskeamiseen on githubissa open mahtulla 

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")

###tehtävä on muuta nää kaikki sun omalla tähtillä eli muodusta jokin uus
 ### checkatka se M merki kansioiden perässä 
  ### jakauta se kaikki kansiot git hubii siistesiksi