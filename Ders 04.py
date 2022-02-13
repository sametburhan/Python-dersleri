#operatör önceliği
print(9**3) #üssü
print(12+4*3+4**2)
print(2**3+2*2)

dak = int(input("kaç dakika\n"))
yuzde = (dak)/60
print(yuzde," saat eder")

#hata konusu
y = 5
x = y + 2
# y + 2 = x  bu hatalı satır
# ()3+4)) hatalı satır
# ("hello') hatalı satır
# sola dayalı yazmamak da hataya sebep olur

#celsius dan fahrenheit a dönüşüm
# C = 5/9 x (F - 32)
print("celsius değeri fahrenheit değerine dönüştürülecektir")
c = int(input("celcius değerinizi giriniz = "))
f = (9/5*c)+32
print(f)

#saniye hesaplama
print("gireceğiniz saat değerinin kaç saniye ettiği hesaplanacaktır")
hour = int(input("saat değerinizi girini = "))
second = hour * 60 * 60
print("girdiğiniz değer "+str(second)+" eder")

#saniyeyi saat, dakika ve saniye türüne çevirme
print("gireceğiniz saniye değeriniz saat dakika ve saniye türünden yazılacaktır")
san = int(input("lütfen sayi değerinizi giriniz = "))
saat = san // 3600
saatmod = san % 3600#mod
dakika = saatmod // 60#kaç tane var
dakikamod = saatmod % 60
saniye = dakikamod
print("girmiş olduğunuz değer = "+str(saat)+" saat "+str(dakika)+" dakika "+str(saniye)+" saniye")