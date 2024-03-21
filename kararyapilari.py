ortalamaNot=int(input("lütfen ortalamanızı giriz:"))
#print(type(ortalamaNot))

if ortalamaNot > 80:
    print("Bravo")
elif ortalamaNot > 50:
    print("başarılı")    
    if ortalamaNot > 40:
        print("Normal")
else:
    print("Dersten Kaldınız ")    
print("if - else bloğu içerisinde miyim? "  )