import random

r = random.randint(20,50)
print(r)



for i in range(r):
    if (i+1) % 10:
        print(i + 1)
    else:
        print('뽀숑')


print(list(range(3, 10, 3)))
