#sadece çağırıldıklarında çalışan kod parçalarıdır
#definition => tanımlama
def ortalamaHesapla():
    vize =85
    final =90
    ortalama=(vize*0.4)+(final*0.6)
    print(ortalama)   

def ortalamaHesapla2():
    vize =100
    final =100
    ortalama=(vize*0.4)+(final*0.6)
    print(ortalama)
    return ortalama #fonk çağırıldığı yere götürür 

ortalamaHesapla()
print (ortalamaHesapla2())

def ortalamaHesapla3(vize:float,final:float)->float:
     return (vize*0.4)+(final*0.6)

print(ortalamaHesapla3(78,98))


exam1=int(input("Vize notunuzu giriniz: "))
exam2=int(input("Final notunu giriniz: "))
def ortalamaHesapla4(vize:float,final:float)->float:
    return (vize*0.4)+(final*0.6)

print(ortalamaHesapla4(exam1,exam2))
