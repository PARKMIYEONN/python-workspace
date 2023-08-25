# 패스워드 변경서비스

members = {'aaa': '1111', 'bbb': '2222', 'ccc': '3333', 'ddd': '4444'}
print('패스워드 변경서비스입니다')
id = input('아이디를 입력하세요 : ')

if id not in members:
    print(f'입력하신 아이디 [{id}]는 존재하지 않습니다')
    print(f'패스워드 변경서비스를 종료합니다')
    exit(0)

password = input('현재 패스워드를 입력하세요 : ')
if members.get(id) != password:
    print('패스워드가 일치하지 않습니다')
    print('서비스를 종료합니다')
    exit(0)

newPassword = input('변경할 패스워드를 입력하세요 : ')
# members.update(id=newPassword) 이 방식은 문제가 있음. id를 변수가 아닌 하나의 문자열로 인식함.
# members.update([[id, newPassword]])     # key를 변수로 쓰는 경우에 update함수는 조심해서 써야 함
# members.update({id:newPassword})
members[id] = newPassword

print('< 전체 회원 목록 >')
for id, password in members.items():
    print(f'{id} : {password}')

# if id in members:
#     pass
# else:
#     print(f'입력하신 아이디 [{id}]는 존재하지 않습니다')
#     print(f'패스워드 변경서비스를 종료합니다')
