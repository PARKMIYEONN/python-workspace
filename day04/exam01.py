# data = set() # 그냥{}이렇게 적으면 dict로 인식하기 때문에 빈 set을 만들어주려면 이렇게 적어야 함
data = set([1, 2, 3, 4])
data2 = {1, 4, 5, 6}
print(type(data), data)
print(type(data2), data2)

print(f'합집합(data, data2) : {data.union(data2)}')
print(f'연산자 | 를 사용한 합집합(data, data2) : {data | data2}')

print(f'교집합(data, data2) : {data.intersection(data2)}')
print(f'연산자 & 를 사용한 교집합(data, data2) : {data & data2}')

print(f'차집합(data, data2) : {data.difference(data2)}')
print(f'연산자 - 를 사용한 차집합(data, data2) : {data-data2}')

print(f'대칭차집합(data, data2) : {data.symmetric_difference(data2)}')
print(f'연산자 ^ 를 사용한 대칭차집합(data, data2) : {data^data2}')

print(data, data2) # 원본 데이터는 바뀌지 않는다

#set형은 [0]등 인덱스를 쓸 수 없다. [:]사용 불가