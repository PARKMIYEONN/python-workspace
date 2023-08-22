data = list(range(1, 10))
print(data)

print(data[0]) #0번지의 데이터

print(data[0:5]) #0, 1, 2, 3, 4번지의 데이터. 뽑아내서 따로 리스트의 집합으로 가지고 있는 것. 데이터가 바뀌는 것은 아님
data2 = data[0:5]
print(data)
print(data2)
print(data[5:8])
print(data[:3]) #말하지 않으면 시작 값이 0이라고 인식
print(data[3:]) #print(data[3:len(data)])
print(data[:])

print(data)
#data2 = data   #Shallow copy
data2 = data[:] #Deep copy, 주소값만 복사하는 게 아니라 새롭게 만듦, 아이디가 달라!
print(data2)
data2[0] = 100

print('data2 :', data2, id(data2))
print('data : ', data, id(data))

print(data[5:len(data)])
print(data[5:-1]) #len(data)-1 라는 의미라고 생각하면 됨
#리스트명[시작=0:종료=len(리스트):간격=1]
print(data[2:8:2])
print(data[2::2])
print(data[8:2:-2])
print(data[::-1]) #거꾸로 할 때 복잡하잖아. -1일 땐 다 생략 가능해. 알아서 끝에서부터 역순이라는 뜻을 가지고 있어
print(data[::-3])

print('data : ', data)
# data[15] = 100
print('data : ', data) #이미 있는 데이터만 가지고 접근 가능. 인덱스가 벗어났잖아 지금...

# data[2:5] = [100, 200, 300]
# data[2:5] = [100] # 이렇게 넣으면 배열의 length가 바뀜
# data[2:5] = [100, 200, 300, 400, 500]
data[2:6:2] = [10, 20]
print('data : ', data)

# del data[2:3]
del data[2:5]   #튜플은 읽기 전용이라 그 안의 데이터를 삭제하거나 수정하는 건 불가. 리스트로 변환해서 바꾸거나 해야됨.
print('data : ', data)