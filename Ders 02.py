sayi=10
print(sayi)
print("merhaba dünya")
print(12+int('12'))
print("merhaba"+str(" merhaba"))
print(type(int("32")))
x=14
y=32
print(str(x+y))
print(str(float(12.3)))

#değişken tanımlaması aşağıdaki şekilde yapılabilir
x, y, z = 10, 20, 30
print(x+y+z)

a= 19
print("seçtiğiniz sayı bu =",a,"ve seçtiğiniz sayının türü de bu =",type(a))

#del komutu değer silmek için kullanılır fakat dil sırasıyla ilerlediği için önceki satırlara müdehale edemez
#float reel sayıdır
d = 34.23
print(type(d))
print(int(d)) #yuvarlama yaparak değeri yazdırır
e=3.45
f=str(e)
print(f)

#round kodu virgüllü sayıları yuvarlar
g=45.78
print(round(g))
# 76543210123456789   aşağıda yazılan 2. sayı soldaki basamak değerine kadar yuvarlanır
h=3423423.567023452
print(round(h, 3))
print(round(h, 1))
print(round(h, 8))
print(round(h, 6))
print(round(h, 0))
print(round(h, 1))
print(round(h, -7))
print(round(h, -4))
print(round(h, -1))

elit_insanlar="kimler" #boşluk yerine alt çizgi kullanabilirsin
print(elit_insanlar)