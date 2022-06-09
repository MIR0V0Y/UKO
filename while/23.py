import random
A = random.randrange(1,1000)
B = random.randrange(1,1000)
print("A = {0}, B = {1}".format(A,B))
while B > 0:
    A,B = B,A%B
print("НОД: ",A)