#solid prensibleri (araştırma)

#for 
#start => başlama noktamız (defaultu: 0)
#stop => nerede duracağımız
#step => döngü kaç kaç artsın (defaultu: 1)
""" for i in range(1,10):
    print(i) """


""" #kullanıcının girdiği sayılar arasında en büyüğü bulmak
biggestValue = 0
for i in range(3):
    sayi = int(input(f"sayiyi giriniz: "))
    if sayi > biggestValue:
        biggestValue = sayi

print(f"Girdiğiniz sayilar arasindan en büyüğü: {biggestValue}") """

#diziye eleman ekleme
""" sayilar = []
for i in range(3):
    sayilar.append(int(input(f"sayiyi giriniz: ")))

sayilar.sort(reverse=True) #büyükten küçüğe sıralamak istiyorum
print(sayilar)
print(max(sayilar)) """

students = ["Demet", "Yağmur", "Zeynep", "Tuğçe"]
print(len(students))

for i in range(len(students)):
    if i >1:
        break #ilgili döngünün o anda kırılmasını sağlar 
    print(f"{i+1}. Öğrenci: {students[i]}")

for student in students:
    if student == "Yağmur": #bir sonraki ile devam et
        continue
    print(f"Ogrenci: {student}")