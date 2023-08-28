data = set()
print(f'{data} 원소의 개수 : {len(data)}')
for i in range(10):
    data.add(i+1)

data.add(5) # 중복 불가

data.add('5') # 자료형이 다르면 가능

print(f'{data} 원소의 개수 : {len(data)}')

data.remove('5')
print(f'remove("5") 후 {data} 원소의 개수 : {len(data)}')
# data.remove('5')  # 없는 것을 지우려면 에러가 남. 쓰기 전에 있는지 없는지 if문으로 예외 처리 필요

data.discard('5')
print(f'discard("5") 후 {data} 원소의 개수 : {len(data)}')
data.discard('5')

data.discard(5)
print(f'discard(5) 후 {data} 원소의 개수 : {len(data)}')  #없더라도 예외가 발생하지 않음.

copy = data         #얕은 복사
copy = data.copy()  #깊은 복사
print(f'data : {data}')
print(f'copy : {copy}')

copy.add(5)
print(f'data : {data}')
print(f'copy : {copy}')


