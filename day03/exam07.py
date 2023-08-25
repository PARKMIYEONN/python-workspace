#정수 2개 입력받아 최대공약수 출력

num1, num2 = input('두 개의 정수 입력 : ').split()

no1 = int(num1)
no2 = int(num2)

data1 = [i for i in range(1, no1 + 1) if not no1 % i]
