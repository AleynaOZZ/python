print("merhaba dünya ")

#değişkenler=>herhangi bir veri içeren ifadedir
#string=> Metinsel ifadeler
text="Merhaba , hos geldin "
fullName="Aleyna" #veri tabanından bilgi alınıyor
print(text +fullName)#Anasayfa
print(text)#profilim 
print(text)#aabout
print(text)#contact

#int,integer  tam sayı 
studentCount = 45
print(studentCount + 5)

#double,decimal,float => ondalıklı sayılar 
averagePoint =25.5
print(averagePoint+5)

#bool,boolean =>true-false sonuç döndüren yapılat
isVeriFied=True
print(isVeriFied)



print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVeriFied))


#matematiksel operatörler
# + - / * %
number =10 
print(number+ 10)

print(number-5)

print(number*2)

print(number/2)

print(number%3)

#mantıksal operatörler =>karşılaştırma operatörleri
print(number == 10)#true
print(number == 11)#false

print(number!= 10)#false 
print(number!= 11)#true

print(number > 10)#false
print(number >=10)#True

print(number < 10)#False
print(number <=10)#true

#stringinterpolation => metin birleştirme
print(text +fullName)#Anasayfa
#f-string
totalText = f"Hoşgeldiniz {fullName}"
print(totalText)