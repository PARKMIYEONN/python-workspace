'''
num01 = input('첫번째 정수 입력 : ')
num02 = input('두번째 정수 입력 : ')
print(num01, num02)
'''


print(type('12, 5'.split()))
num01, num02 = map(int, input('두 개의 정수를 입력 : ').split(':')) # 여러개의 데이터를 입력받을 때 둘 다 형변화해줄 때 사용.

# num01, num02 = input('두 개의 정수를 입력 : ').split() #split에 아무것도 붙지 않으면 공백으로 나눈다는 뜻
                                                    #배열에 알아서 들어감
print(num01, num02)
print(type(num01), type(num02))