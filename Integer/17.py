import random
N = random.randrange(1000,1000000)
print("Число: ", N)
d1 = int(N/100)
d2 = d1%10
print("Деление на 100: ", d1)
print("Остаток от деление на 10: ", d2)
print("Цифра в сотне: ", d2)