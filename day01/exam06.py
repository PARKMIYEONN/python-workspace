num = int(input('정수 입력 : '))
if num > 0:
    if num % 2: #이 수가 0이 아닌 경우에 참의 값이 나오기 때문에 이때 경우가 홀수가 된다
        print(num, ': 홀수')
    else:
        print(num, ': 짝수')
else:
    print('짝홀판단안됨')

if num < 0:
    print(f'{num} : 음수')
elif num == 0 :
    print(f'{num} : 0')
elif num % 2 == 0 :
    print(f'{num} : 짝수')
else:
    print(f'{num} : 홀수')


if num < 0:
    print(f'{num} : 음수')
elif num == 0 :
    print(f'{num} : 0')
elif num % 2 : #이 수가 0이 아닌 경우에 참의 값이 나오기 때문에 이때 경우가 홀수가 된다
    print(f'{num} : 홀수')
else:
    print(f'{num} : 짝수')


# import random
#
# r = int(random.random() * 10) # 0~9사이 숫자 출력
# print(int(random.random() * 10))
#
# if r % 2 == 0:
#     print(f'{r} : 짝수')
# else:
#     print(f'{r} : 홀수')