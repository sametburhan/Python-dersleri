print(12,"samet")#virgül kullanmak yan yana yazılan string ve integer ifadelerin hata vermesini engeller ve aralarına 1 adet boşluk koyar

#saniyeyi saat, dakika ve saniye türüne çevirme
print("gireceğiniz saniye değeriniz saat dakika ve saniye türünden yazılacaktır")
san = int(input("lütfen sayi değerinizi giriniz = "))

saat = san // 3600
saatOnlar = saat//10
saatBirler = saat%10
saatmod = san % 3600#mod

dakika = saatmod // 60#kaç tane var
dakikaOnlar = dakika//10
dakikaBirler = dakika%10
dakikamod = saatmod % 60

saniye = dakikamod
saniyeOnlar = saniye//10

saniyeBirler = saniye%10
print("girmiş oldduğunuz değer = ", end = "")
print(saatOnlar, saatBirler, ":", sep = "", end = "")#saat
print(dakikaOnlar, dakikaBirler, ":", sep = "", end = "")#dakika
print(saniyeOnlar, saniyeBirler, sep = "")#saniye

#sep = "" bu kod virgül sebebiyle oluşan boşluğu yok ediyor ve yerine tırnak içinde ne isteniyorsa onu koyuyor
#end = "" bu kod print kodunun aşağı satıra geçme isteğini engelliyor diğer print kodunun da aynı satırda ekrana yazılmasını sağlıyor
#ayrıca sep kodu gibi tırnak içinde ne isteniyorsu o virgülün koymak istediği boşluğun yerine konuluyor

#aritmetik ifadeler
sayi1 = 8
print(sayi1)
sayi1 += 12 #bu kod sayının son değerine istenilen miktarda sayı eklemeyi çıkarmayı bölmeyi çarpmayı sağlar
print(sayi1)
print(++sayi1) #burada sayıya 1 eklemesini istediğim halde kod sayı üstünde herhangi bir oynama yapmadı
sayi1 -= 2
print(sayi1)
sayi1 /= 6
print(float(int(sayi1)))
sayi1 *= 12
print(str(sayi1))