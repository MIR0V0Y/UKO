import random
i = random.randrange(1,12)
print("Номер месяца: ", i)
i = str(i)
m = {
    '1': 'зима',
    '2': 'зима',
    '3': 'весна',
    '4': 'весна',
    '5': 'весна',
    '6': 'лето',
    '7': 'лето',
    '8': 'лето',
    '9': 'осень',
    '10': 'осень',
    '11': 'осень',
    '12': 'зима'
}
try:
    print(m[i])
except KeyError as e:
    print('Ошибка')