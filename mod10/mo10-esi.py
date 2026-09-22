# .   association  تنقسم ل
# composition التركيب
# person(name , add , email , phone , Date dop)      Date (day , month , year)
#  aggregation  التجميع
# collge (department , semester , year , Stu)    student ( roll nuber , name , marks , totoa )


class Date:

    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

    def set_date(self):
        self.day = int(input("Enter day (1-31): "))
        self.month = int(input("Enter month (1-12): "))
        self.year = int(input("Enter year (e.g. 1998): "))

    def get_date(self):
        return f"{self.day}/{self.month}/{self.year}"


class Persone:

    def __init__(self):
        self.fname = None
        self.lname = None
        self.name = None
        self.addres = None
        self.phone = 0
        self.dob = Date()  # composition

    def set_per(self):
        self.fname = input("enter your first name : ")
        self.lname = input("enter your last name : ")
        self.name = self.fname + " " + self.lname
        self.addres = input("Enter your full addres : ")
        self.phone = float(input("Enter your number : "))
        print("--- Enter Date of Birth ---")
        self.dob.set_date()  # استدعاء دالة تعبئة التاريخ               #Composition (التركيب): كائن ينشأ داخل كائن آخر.
                                                              # (مثال: الشخص وتاريخ ميلاده self.dob = Date()). إذا حذفنا الشخص يختفي تاريخ ميلاده معه.

    def get_per(self):
        print(f"first name : {self.fname}")
        print(f"last name : {self.lname}")
        print(f" name :{self.name}")
        print(f"phone num : {self.phone}")
        print(f"addres : {self.addres}")
        print(
            f"date of birth : {self.dob.get_date()}"
        )  # إظهار تاريخ الميلاد المخزن

    def first(self):
        return self.fname

    def last(self):
        return self.lname


class Employ:

    def __init__(self):
        self.id = 0
        self.salary = 0
        self.email = None

    def set_emp(self):
        self.email = input("Enter your email addres : ")
        self.salary = float(input("Enter your monthly salary : "))
        self.id = float(input("Enter your id number : "))

    def get_emp(self):
        print(f"Email : {self.email}")
        print(f"Salary : {self.salary}")
        print(f" ID :{self.id}")


# --- الجزء التنفيذي ---
p1 = Persone()
p1.set_per()


emp1 = Employ()
emp1.set_emp()

dat1 = Date()
dat1.set_date()


print("\n---person details --- ")
p1.get_per()
print("\n---Employ details --- ")
emp1.get_emp()
print("\n---Date details --- ")
print(dat1.get_date())  # وضعنا print حتى يظهر الناتج على الشاشة

#1. إعادة استخدام الكود وعدم التكرار (Reusability)
#بدلاً من إعادة كتابة متغيرات اليوم والشهر والسنة ودوال إدخالها وطباعتها داخل كل كلاس نحتاجه، نكتب كلاس Date مرة واحدة فقط، ثم نستخدمه داخل أي كلاس آخر بحاجة لتاريخ.

#كلاس Person يحتاج تاريخ ميلاد ⬅️ self.dob = Date()

#كلاس Invoice (فاتورة) يحتاج تاريخ إصدار ⬅️ self.issue_date = Date()

#كلاس Employee يحتاج تاريخ تعيين ⬅️ self.hire_date = Date()

#2. تقسيم الكود وتنظيمه (Modular & Clean Code)
#بدلاً من أن يكون كلاس Person ضخماً ويحتوي على عشرات المتغيرات والدوال، نقوم بتقسيم المسؤوليات:

#كلاس Date مسؤول فقط عن التواريخ وتنسيقها.

#كلاس Person مسؤول فقط عن بيانات الشخص.

#هذا يجعل الكود أسهل في القراءة، وأسهل في التعديل أو إصلاح الأخطاء مستقبلاً.

#3. التحكم الكامل في ملكية ودورة حياة الكائن (Lifecycle Ownership)
#الـ Composition تضمن أن الكائن التابع مرتبط وجودياً بالكائن الأساسي:

#تاريخ الميلاد لا يوجد في النظام بدون الشخص صاحب هذا التاريخ.

#بمجرد إنشاء كائن الشخص p1 = Person()، يتم إنشاء تاريخ ميلاده تلقائياً في الذاكرة.

#إذا قمت بحذف الشخص من الذاكرة، يتم حذف تاريخ ميلاده معه تلقائياً، مما يحافظ على نظافة الذاكرة ومنع البيانات الضائعة (Orphan Data).
