n = int(input("Введите количество дней: "))
i = 1
a = 10
p = 10
while i<n:
    i = i + 1
    a = a + (a*0.1)
    p = p + a
print ( "Спортсмен пробежал " ,p, " км" )