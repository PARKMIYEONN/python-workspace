'''
    List 내장함수
    append : 데이터 추가(맨 마지막)
    insert : 데이터 추가(특정 위치)
    pop : 데이터 삭제(맨 마지막)
    remove : 데이터 삭제(특정 데이터)
    index : 특정값의 위치 검색
    count : 특정값의 빈도수
    reverse : 위치 반대로 뒤집기
    sort : 정렬
    clear : 모두 삭제
'''

data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print(data)
print(data, id(data))   #새로 만들어 지는 것이 아니라 원래 있던 것에 추가하는 것이기 때문에 주소값이 같음!
delData = data.pop()
print('삭제된 값 : ', delData)

data = list()
data.insert(0, 10)
data.insert(0, 20)
data.insert(0, 30)
print(data, id(data))
delData = data.pop()
print('삭제된 값 : ', delData)

data = []
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData = data.pop(0)
print('삭제된 값 : ', delData)

data = [10, 20, 30, 40, 30]
idx = data.index(30)
cnt = data.count(20)
print('위치 : ', idx)
print('개수 : ', cnt)
print('before : ', data)
data.remove(30) #index의 방식과 같이 앞에 하나만 지워지고 하나는 남아있게 됨
print('after : ', data)

for i in range(len(data)):
    print(data[i], end=' ')
print()

for d in data:
    print(d, end=' ')
print()

ite = iter(data)
print(ite) #객체만 나옴
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))

for d in iter(data):
    print(d, end=' ')
print()

data.reverse()  # 내 리스트 자체를 뒤집어버림
for d in iter(data):
    print(d, end=' ')
print()
data.reverse()

for i in range(1, len(data)+1):
    print(data[-i], end=' ')
print()

data2 = reversed(data)
print('data : ', data)  # reversed함수는 원본을 수정하지 않고 새로운 뒤집어진 객체를 만들어줌
print('data2 : ', next(data2))

for d in reversed(data):
    print(d, end=' ')
print(data)

# data.sort()
# print(data)

print(sorted(data, reverse=True)) #True일때 내림차순, 디폴트 속성 : False
print(data)

data = [10]
print(data.pop())
# print(data.pop()) 모자라서 에러남!!

data = [10, 20, 30]
# for i in range(len(data)):
#     data.pop(0)
# data.clear()
# del data[:]
# print(data)

for index, d in enumerate(data, start=100): #시작값을 임의의 값을 넣어주는 방식으로 제어 가능. 디폴트는 0
    print(f'[{index}] : {d}')
print()


