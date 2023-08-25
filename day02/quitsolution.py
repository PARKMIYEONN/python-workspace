print('정수를 입력하세요. quit 입력 시 종료')
inputs = list()
while True:
    data = input()
    if data.lower() == 'quit':  #입력받은 data를 전부 소문자로 바꿔줌. 올바르게 입력하면 모두 체크.
        break
    inputs.append(int(data))

for num in inputs:
    div = [i+1 for i in range(num) if num % (i+1) == 0]
    print(f'{num}의 약수 : {div}')