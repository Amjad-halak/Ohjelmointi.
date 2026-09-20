# THE OOP  == (طريقه لكتابه الكود)
# عام موجود بعده لغات في البرمجه 
# the class in general 
# __init__ (تهيء الداتا للشي الي بدك تعمله )

# in funktion u can leave the parameter empty but not here in class and init ==> mean 
#def member ()
#class Name :
    #def __init__(self , Other_data) :   {it gonna show eror if u leave parameter without SELF and continue normal }



class member : 

    def __init__(self , first_name , middle_name , last_name ,gender) :

        self.fname=first_name   

        self.mname=middle_name

        self.lname=last_name

        self.gender=gender


    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title (self) :
        if self.gender == "women" or self.gender == "nainen ":
            return f"MS : {self.full_name()}"
        elif self.gender == "man" or self.gender == "mies ":
            return f"MR: {self.full_name()}"
        else:
             return f"{self.full_name()}"

    

member_one = member("amjad","mohamad ","alhalak" , "man")
member_Two = member("rama" ,  "mohamad" , "halak" , "women")
member_Three = member("maisa" ,  "ghaza" , "fajer" , "-")


print(member_one.fname,member_one.mname,member_one.lname)
print(member_Two.mname)
print(member_Two.name_with_title())
print(member_one.name_with_title())
print(member_Three.name_with_title())



#=============================
class ikäisyys :
    def __init__ (self , year , ):
        self.year=year
        self.month=year * 12 
        self.days=year * 365
year0=int(input("how old are u ?: "))
amjad=ikäisyys(year0)
typi = input("in which way want your old be (year / month / days ) : ")
if typi == "year":
    print(amjad.year)
elif typi == "month":
    print(amjad.month)
elif typi == "days":
    print(amjad.days)




  
class cat :
    def __init__(self , name , ikä , tyypi , pituus):
        self.name=name
        self.ikä=ikä
        self.tyypi=tyypi
        self.pituus=pituus
    def tall (self):
        if self.pituus > 60 :
            return f" kissasi on aikuinen"
        else:
            return f"kissasi on pikku nuori "
    
cat1=cat("shbshb" , 2 , "domaestic shrthair" , 50 )
cat2=cat("satoor" , 5 , "laperm" , 100 )


print(cat1.name)
print(f"{cat2.pituus} ja sen tyypi {cat2.tyypi} and {cat2.tall()}")        





class lion:

    tehty = 0
    def __init__(self, tyypi, hiuksenpituus, paino, aani="RROOAAARR!"):
        self.tyypi = tyypi
        self.hiuksenpituus = hiuksenpituus
        self.paino = paino
        self.aani = aani

        lion.tehty += 1


lion1 = lion("Afrikanleijona", "Pitkä ja tuuhea harja", 190)
lion2 = lion("Aasianleijona", "Lyhyt harja", 160, "RRAARR!")
lion3 = lion("Berberileijona", "Erittäin pitkä tumma harja", 230, "GROOOAAARRR!")

# التعديل هنا: استخدام النص المصحح والوصول للقيمة الافتراضية عبر lion1.aani
print(f"If the aani parameter is not written (like in lion1), Python will default to writing: {lion1.aani}")

print(f"lion1 kaikki tiedot on {lion1.tyypi} , {lion1.hiuksenpituus} hiukset , {lion1.paino} kg , sen ääni {lion1.aani}")
print(f"lion2 kaikki tiedot on {lion2.tyypi} , {lion2.hiuksenpituus} hiukset , {lion2.paino} kg , sen ääni {lion2.aani}")
print(f"lion3 kaikki tiedot on {lion3.tyypi} , {lion3.hiuksenpituus} hiukset , {lion3.paino} kg , sen ääni {lion3.aani}")

# طباعة عدد الأسود الإجمالي للتأكد من عمل العداد
print(f"Leijonia on luotu yhteensä: {lion.tehty}")



#class samakaltainen kun blueprint (عنا شخصيه بدنا ننشألها عمر, صحه, سرعه )
class charecter :
    def __init__ ( self , health , damage , speed ):   # self هون ثابته دايما بلمعادله 
        self.health=health
        self.damage=damage
        self.speed=speed
    def douple_speed(self):
        self.speed *= 2 
warrior=charecter(100 , 50 ,10 )
ninja=charecter( 80 , 40 , 60 )


print(f"warrio speed is {warrior.speed}")
print(f"ninja speed is {ninja.speed}")

warrior.douple_speed()

print(f"warrio speed is {warrior.speed}")
print(f"ninja speed is {ninja.speed}")

ninja.douple_speed()
print(f"warrio speed is {warrior.speed}")
print(f"ninja speed is {ninja.speed}")

#===========================




