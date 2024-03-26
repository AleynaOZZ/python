class StudentOdev:
    #attribute,property,field
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print("Yapıcı bloklar çalıştı")

    #method, davranışlarımızı
    def doHomework(self, message):
        print(f"{self.name}: {self.age} yaşında, {message}")

    def study(self):
        print(f"{self.name} is studying....")

StudentOdev1 = StudentOdev("Fatma",25)  # İnstance(örnek oluşturuyorum)
StudentOdev1.doHomework("Ödevi yaptım")
StudentOdev1.study()