members = {'홍길동': '1111-2222', '박길동': '3333-4444', '윤길동': '5555-6666'}

print(f'홍길동 존재여부 : {"홍길동" in members}')
print(f'고길동 존재여부 : {"고길동" in members}') # in은 value는 추적 불가. key값으로만 판단 가능
print(f'전화번호 존재여부 : {"1111-2222" in members}')  #value라서 in으로 판단 불가


print(members.keys())   #list
print(members.values()) #list
print(members.items())  #tuple을 원소로 갖고있는 list

for data in members:
    # print(data, end=' ')  #key만 나와...
    print(f'{data} : {members.get(data)}')
print()

for data in members.keys(): #좀 더 직관적인 형태. key만 나온다고 보기만 해도 알 수 있다.
    print(data, end=' ')
    # print(f'{data} : {members.get(data)}')
print()

for data in members.values():
    print(data, end=' ')
print()

# for key, value in members.items(): #tuple의 형태로 뽑아내서 key와 value를 각각 받을 수 있다.

a, b = [2, 3]   #list에 있는 값을 변수에 순서대로 각각 할당한다
print(f'a:{a}, b:{b}')

for key, value in members.items():
    print(f'{key} : {value}')

keys = ['name', 'age', 'addr']
mem = dict.fromkeys(keys, "") #keylist를 통해서 dictionary를 만드는 함수
print(mem)

