
from SelfYapısıOgrenci import StudentOdev # Örnek bir modül adı kullandım
from SelfYapısıTeacherÖdev import Teacher

studentList=[]
teacherList=[]

student1=StudentOdev("Aleyna",22)
student2=StudentOdev("Gözde",22)

teacher1=Teacher("irem","analist")
teacher2=Teacher("Denizhan","Test")

def add(type,obj):
    if type=="student":
        studentList.append(obj)
    else:
        teacherList.append(obj)

def getAll(type):
    if type==  "teacher":
        for teacher in teacherList:
            print(teacher.name)
    else:
        for student in studentList:
            print(student.name)

add("student",student1)            
add("teacher",teacher1)
add("student",student2)
add("teacher",teacher2)

getAll("student")
getAll("teacher")

print(studentList)
print(teacherList)
