class NotEvenException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def get_number():
    num = int(input('짝수를 입력하세요 : '))
    try:
        if num % 2:
            raise NotEvenException(f'{num}은 짝수가 아닙니다')
    except Exception as e:
        print('get_number() 예외발생')
        raise  # 이미 예외가 발생함. 그 예외를 또 떠넘기고 싶을 때 raise만 적으면 다시 넘길 수 있음.
    return num

try:
    num = get_number()
    print(num)
except NotEvenException as e:  #호출했던 곳까지 가서 예외처리를 함. 거기까지 갔는데 예외처리가 없으면 파이썬의 예외처리가 작동함.
    print(e)