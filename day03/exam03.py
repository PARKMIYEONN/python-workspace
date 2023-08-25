'''
    setdefault  새데이터 삽입
    update      key 없으면 데이터 삽입, key 있으면 데이터 수정
    pop         데이터 삭제
    clear       데이터 전체 삭제
'''

members = {'홍길동':'010-1111-2222', '박길동':'010-3333-4444'}
print(members)
members.setdefault('윤길동', '010-5555-6666') # 새로운 키밸류 추가
members.setdefault('이길동')   # 밸류를 지정해주지 않으면 None이라는 값이 들어감
print(members)

members.setdefault('이길동', '010-7777-8888')  # 새로운 원소값을 삽입할 목표로만 사용됨. 기존의 데이터를 수정할 수 없음
print(members)

# members.update(key=value) 수정하는 방법
members.update(이길동='010-7777-8888')

members.update(한길동='010-9999-0000') #없는 데이터를 업데이트하면 새로운 데이터를 추가하게 됨
                                    # =로 작성되는 방식은 key가 문자열일 때만 가능함. 따라서 update는 여러 옵션을 제공.
members.update({2023082501:'010-2345-6789'})
members.update([[2023082502, '010-1234-5678'], ['고길동', '010-4567-8901']])
print(members)

members.update(zip(['park', '이길동'],['8282', None]))
print(members)

value = members.pop('이길동')
print(f'pop("이길동" : {value})')  #pop을 사용하면 입력된 key에 해당하는 value값이 리턴됨.
value = members.pop('구길동', "없음")    # key값이 존재하지 않을 때 리턴할만한 값을 뒤에 적어주면 됨
print(f'pop("구길동" : {value})')
print(members)

members.popitem()   #스택처럼 작동함. 가장 마지막 값이 삭제됨. 이전 버전은 다르게 작동할 수 있음(랜덤하게 하나 지우기).

print(members)

value = members.get('홍길동')  #홍길동이라는 key값에 해당하는 value가져오기
print(f'홍길동 : {value}')
print(f'이길동 : {members.get("이길동", "없는 사원입니다")}')    #없는 값일 경우 None이 아닌 값 지정해주기