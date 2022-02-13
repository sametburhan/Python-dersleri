x = 12
if x==20:
    print("x 20 dir")
else:
    pass
#else içini boş bıraktı


#and ve or matematikte kullanıldığı anlama sahip
a = 10
b = 20
y = (a ==10 and b == 20)
print(y)
y = (a == 20 and b == 20)
print(y)
y = (a == 20 and b == 10)
print(y)
y = (a != 20 or b <= 20)
print(y)
y = (a >= 20 or b != 10)
print(y)
y = (a == 20 or b==10)
print(y)

#kayar nokta hesaplama
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print(d1)
print(d2)
if d1 == d2:
    print("aynı")
else:
    print("farklı")