'''
    def 함수(인자, 인자, ...):
        문장
        문장
        ...
        return
'''
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print(f'덧셈 : {add(12,7)}')
print(f'뺼셈 : {sub(12,7)}')
print(f'곱셈 : {mul(12,7)}')
print(f'나눗셈 : {div(12,7)}')

def calculate(a, b):
    return add(a, b), sub(a, b), mul(a, b), div(a, b)

print(calculate(12, 7)) #튜플 형태로 리턴됨

a, b, c, d = calculate(12, 7)   #언패킹 방식으로 가능하다