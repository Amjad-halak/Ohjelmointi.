def hello_funk():
    pass       #هي ال (pass)بتعني انو مابدنا نعمل اي شي فيها لل funktion هلق بس ممكن نعدل عليها بعدين مشان ما تسبب مشاكل ك (ohjelma kaatu Terminaliss).
print("-" * 20 )

print(hello_funk())    # النتيجه حتكون (None)  لان مافي شي بلداله تبعنا .

def hello_funk():
    print("i hate python ! ")    

hello_funk()         # => تطيع ال (i hate python)
print(hello_funk())   # => تطيع ال (i hate python) +
                                    # => (None )  (Return)   السبب في طباعه الداله مافيها 
print("-" * 20 )

# استخدام الدالو انو احسن ما نطبع ونعدل داخل الطباعه منقوم بلتعديل داخل ال الداله (funktion) 
# يعني 
def hello_funk():
    print("i hate python ! ")          #بدنا نعدل التعجب لنقطه  (طالب من اطبع ١٠٠ مره)  

#hello_funk()   
# 1)     
print("i hate python . ")        # اعدل كل وحده لحالها  
print("i hate python . ")
print("i hate python . ")
print("i hate python ! ")
print("i hate python ! ")

# 2) اعدل الداله فقط واستدعي الداله بسهوله  
print("-" * 20 )
def hello_funk():
    print("i hate python . ")          # بعدلا ل داله لحاله وبستدعي 

hello_funk()   
hello_funk()   
hello_funk()   
hello_funk()   

print("-" * 20 )
# return 

def hello_funk(): 

    print("i hate python . ")          # print  وظيفتها فقط عرض النتيجة للمستخدم على الشاشة. النتيجة تختفي فوراً ولا يمكنك حفظها في متغير أو استخدامها في حسابات أخرى

hello_funk() 


def hello_funk():

    return "i hate python . "         #return وظيفتها إعطاء النتيجة للبرنامج نفسه. الدالة تحسب الحسبة وتُرجع لك الرقم النهائي لتخزنه في متغير، أو تستخدمه في عمليات أخرى، أو تطبعه متى تشاء.
      

print(hello_funk())

print("-" * 20 )

def TT(grooth , name = "et kirjoitanut !!"):             # (et kirjoitanut ) تظهر في حال ماكتب اسمه وقت طباعه الداله
    return f"{grooth} , nimisi {name} function ! "  # الـ f تكون خارج علامات التنصيص


print(TT("HEI" , "amjad"))  # ممكن اعدل واكتب الي بدي بفضل ال return 



print("-" * 20 )

def laske():

    return 5 + 5        # الدالة تعيد الرقم 10 للبرنامج.   => (laske() )


x = laske()         # الآن المتغير x أصبح يحمل الرقم 10 بشكل دائم!
print(x * 2)        # النتيجة: 20  
print(x*10)         # صار فينا نعدل عل المخرجات 

print("-" * 20 )

            # the (* and ** )in function
            

def student_name(*args , **kwargs):        # تسمحلنا انو 
    return (args , 
            kwargs)

x=student_name("Math" , "History" , Name="amjad" , age =23 , tall=185  )
print(x)

print("*" * 20 )

def student_tiedot(*args , **kwargs):                   # ماشتغلت والسبب هو ال * and **
    return f"kurses : {args}\ninfo: {kwargs}"

course = ["Math" , "History" ]                           # نضيفله * قدام [اليسته] لفك قيمتهن 
tiedot = {"Name":  "amjad" , "age": 23 , "tall": 185}    # نضيفله ** قدام [قاموس] لفك قيمتهن 

course.remove("Math")
course.append("Fysiks")

print(student_tiedot(*course , 
                     **tiedot ))    # نتيجه فارغه

print("-" * 20 )






month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 1. الدالة يجب أن تُرجع True أو False حتى نستفيد منها في الشروط
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    # التصحيح: إذا كان الشهر **خارج** النطاق 1-12 نُرجع الخطأ
    if not (1 <= month <= 12):
        return "invalid month"

    # إذا كان الشهر شباط والسنة كبيسة نُرجع 29
    if month == 2 and is_leap_year(year):
        return 29

    # لغير ذلك نُرجع عدد الأيام من القائمة
    return month_days[month]


# تجربة الكود:
print(days_in_month(2017, 3))  # النتيجة: 31
print(days_in_month(2020, 2))  # النتيجة: 29 (سنة كبيسة)
print(days_in_month(2021, 15)) # النتيجة: invalid month










