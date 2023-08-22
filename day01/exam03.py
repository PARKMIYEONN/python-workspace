# 논리값(True, False) 맨 앞글자 대문자로 적어야 됨

print(True, False)
print(10 > 3)
print(10 == 3)
print(10 != 3)
print("Hello" == "Hello")
print("Hello" == "hello")
print(1 == 1.0) #파이썬은 그냥 값 자체를 비교하기 때문에 같은 애로 인식을 함. 근데 실제로는 아니잖아
print(1 is 1.0) #객체까지 비교해서 같은지 않은지 판단하는 연산자 자바스크립트의 ===같은 것, id에 있는 메모리값까지 비교를 하기 때문
print(id('Hello')) #어느 위치값에 저장이 됐는가 라는 형태를 볼 때 id를 씀
print(id('Hello'))
print(id('hello'))
print(id(1))
print(id(1.0))

print(bool(1), bool('false'), bool(False), False)

print("abc" and "def") # print("abc")를 먼저 보고 and연산자를 써야되니까 뒤의 것도 봐야되잖아 그래서 "def"만 출력이 되는 거야..
msg = "hello" and "안녕" #문자열의 and or는 조금 생각을 해봐야돼
msg = "hello" or "안녕"
print(msg)

print('Hello')
print("""안녕
이
게
된
다
고""")
print('''여러줄
도
가
능''')



