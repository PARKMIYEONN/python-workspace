data = [10, 20, 30, 40] #꼭 같은 데이터의 자료형이 아니어도 리스트 안에 넣을 수 있다. 선언을 해주지 않기 때문
print(type(data), data)
data = list()
print(type(data), data)

data = (10, 20, 30, 40)
print(type(data), data)
data = tuple()
print(type(data), data)

#data = 10
data = 10, 20  #(10,20)으로 인식을 함 #일련의 데이터들을 , 로 나열해서 쓰면 시퀀스 자료형의 읽기 전용 튜플로 인식을 한다
print(type(data), data)

# range(시작=0, 종료, step=1) 종료와 step만 따로 쓸 순 없다. 헷갈리잖아...
data = range(10) #10개의 숫자를 생성해라
print(type(data), data)

data = list(data)
print(type(data), data)

data = range(5, 15)
print(list(data))

data = list(range(1, 10, 2))
print(data)

data = list(range(20, 4, -3))
print(data)
print(16 in data, 17 in data)
print('elo' in 'hello')
print(10 in range(10))

