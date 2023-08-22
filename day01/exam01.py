'''
    정수 2개 입력받아 사칙연산의 결과 출력
'''

print('첫번째 정수를 입력 : ', end='')
num01 = int(input())
# print(type(num01))
print('두번째 정수를 입력 : ', end='')
num02 = int(input())


print(num01, '+',  num02, '=', num01 + num02)
print('%d - %d = %d' % (num01, num02, num01 - num02))
print('%d * %d = %d' % (num01, num02, num01 * num02))
print('%d / %d = %d' % (num01, num02, num01 / num02)) #정수형으로 정해져있어서 정수형으로 결과가 나옴
print('%d / %d = %f' % (num01, num02, num01 / num02)) #실수형으로 정해져있어서 실수형으로 결과가 나옴
print(num01 / num02) #파이썬은 나누기를 하면 자동변환이 되기 때문에 실수형으로 바꿔줌
print('{0} / {1} = {2}'.format(num01, num02, num01 / num02)) #인덱스로 자리 지정
print(f'{num01} / {num02} = {num01 / num02}') #문자를 찍을건데 그 문자를 formating해서 넣겠다?
print(int(num01 / num02)) #몫만 구하고 싶다
print(f'{num01} / {num02} = {num01 // num02}') #형변환 없이 몫만 구할 수 있다
print(f'{num01} / {num02} = {num01 / num02}')
print(f'{num01} % {num02} = {num01 % num02}') #나머지만 구하기
print(2 ** 3) #거듭제곱
print(f'{num01} ** {num02} = {num01 ** num02}')
print('2' * 3) #문자열과 사칙연산이 결합하면 의미가 달라짐. 여기에선 반복의 의미를 가짐

