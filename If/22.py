import random
lst = [i for i in list(range(-10,11)) if i != 0]
for i in range(0,5):
    x = random.choice(lst)
    y = random.choice(lst)
    print("\nТочка (x, y): ({0},{1})".format(x, y))
    print("Координатная четверть: ", end="")
    if x > 0 and y > 0:
        print("I")
    elif x < 0 and y > 0:
        print("II")
    elif x < 0 and y < 0:
        print("III")
    else:
        print("IV")