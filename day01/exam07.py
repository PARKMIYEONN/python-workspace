num=1
while num <= 10:
    print(num, end=' ')
    num += 1

print()

for i in range(10):
    print(i+1, end=' ')

print()

for i in range(10):
    if (i+1) % 2:
        print(i+1, end=' ')

print()

for i in range(0, 10, 2):
    print(i+1, end=' ')

print()

names = ['홍길동', '강길동', '윤길동']
for name in names:
    print(name, end=' ')

print()

for i in range(5):
    print('*' * (i+1))

print()

for i in range(5):
    print(' ' * i, '*' * (5-i), sep='') #공백을 없애주어야 함

print()

for i in range(9):
    if i < 5:
        print('*' * (i+1))
    else:
        print('*' * (9-i))

for i in range(9):
    #참문장 if 조건식 else 거짓문장
    cnt = (i+1) if i < 5 else (9-i)
    print('*' * cnt)















