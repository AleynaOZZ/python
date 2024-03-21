sayilar= [100,200,300,400,"Merhaba"]

print(sayilar)
print(sayilar[1])#diziler sıfırdan başladığı için 200 ü getirir
print(sayilar[0])#programcı saymaya 0 dan başlar

sayilar.append(500) 
sayilar.append(200)# sonuna sayı ekler 
print(sayilar)

sayilar.remove(200) # değere göre silme işlemini gerçekleriştirir 
print(sayilar)

sayilar.pop()#index göre silme işlemi yapar//default index son index
print(sayilar)

sayilar.extend([700,800])
print(sayilar)

sayilar.clear() # => dizi içindeki tüm elemanları siler
print(sayilar)