def myPrint(*values,end='>',sep='\t'):    # *values : 가변 인수, end를 생략한다면 디폴트로 여기에 들어오는 값을 갖게 함
    for value in values:
        print(value, end=end, sep=sep)   # end에 사용하면서 지정해준 end값을 넣어주겠다

#내 함수
# def calc(*values):
#     answer = 0
#     answermul = 1
#     if values[0] == 'add':
#         for value in values[1:]:
#             answer += value
#         return answer
#     if values[0] == 'mul':
#         for value in values[1:]:
#             answermul *= value
#         return answermul

#교수님 함수
def calc(command, *args):
    s = 0 if command == 'add' else 1
    for value in args:
        if command == 'add':
            s += value
        elif command == 'mul':
            s *= value
    return s


myPrint(10)
myPrint(10, 'A')
myPrint((10,20,30,40), [100,200,300,400])

print()

print(calc('add', 12, 7))
print(calc('add', 12, 6, 9))
print(calc('mul', 12, 7))
# print(calc('mul', 12, [6, 9, 10]))    이 문제 생각해보기!!!!!!!!!!!!!!!! 이 상태에서 이 인자들을 어떻게 볼건지?
print(calc('mul', 1, 2, 3, 4, 5))



# print('abc')
# print(10)
# print([1,2,3,4,5],[10,20,30,40,50])
# print(10,20,30,40,'aaa', end='', sep='')

