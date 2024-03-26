class Student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        print("Yapıcı blok çalıştı")

    #method,davranışlarımızı
    def doHomework(self,message):
        print(f"{self.name} {self.age} : {message}")

    def study(self):
        print(f"{self.name} is Studying...")


student1 = Student("Enes",25) #instance(örnek oluşturuyorum)
student1.doHomework("Ödevi yaptım")
student1.study()


student2 = Student("Neşe",25) #instance(örnek oluşturuyorum)
student2.doHomework("Ödevi yaptım")
student2.study()