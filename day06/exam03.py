try:
    num = int(input('짝수를 입력하세요 : '))
    if num % 2:
        raise Exception(f'{num}은 짝수가 아닙니다')
except Exception as e:
    print(e)
else:
    print(f'출력 : {num}')