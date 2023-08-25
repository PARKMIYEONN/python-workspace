'''
    quit가 나올때까지 정수를 입력받아 각 정수의 약수를 출력
    10
    6
    36
    87
    23
    40
    quit
    10의 약수 : [1, 2, 5, 10]
    6의 약수 : [1, 2, 3, 6]
    36의 약수 : [1, 2, 3, 4, 6, 9, 12, 18, 36]
    ...
    40의 약수 : [...]
'''


# for i in range(len(data)):
#     print(data)

data = list()

while True:
    datum = input('데이터 입력. quit 입력시 종료 : ')
    if (datum.lower() == 'quit'):
        break
    else:
        data.append(int(datum))
print(data)
for num in iter(data):
    divisor = [i for i in range(1, num + 1) if not num % i]
    print(f'{num}의 약수 : {divisor}')





