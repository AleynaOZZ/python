"""---Bir okul kayıt sistemi kodlayalım---
Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.
Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki propertylerden yararlanalım."""

class Teacher:
    #attribute,property,field
    def __init__(self, name, lesson) -> None:
        self.name = name
        self.alessonge = lesson
        print("Yapıcı bloklar çalıştı")

    #method, davranışlarımızı
    def classes(self, message):
        print(f"{self.name} is teaching")

    def rest(self):
        print(f"{self.name} is resting...")

teacher = Teacher("Ayşe", "Matematik")
teacher.classes("Derse girdim")
teacher.rest()
