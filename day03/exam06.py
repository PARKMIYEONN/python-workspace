# keys = ['names', 'age', 'addr']
#
# members = {key:value for key, value in dict.fromkeys(keys).items()}
# print(members)

members = {'홍길동':'32거2345', '고길동':'26소2756', '윤길동':'46허1098'}
print(members.get('홍길동'))

# 차량번호 26소 2756의 소유주 검색

mem = {value:key for key, value in members.items()}     # key 와 value를 바꿔줌
print(mem.get('26소2756'))

data = [key for key, value in members.items() if value == '26소2756']    # key값으로 형성된 list를 만들어줄 수 있다.
print(data[0])

# for key, value in members.items():
#     if value == '26소2756':
#         print(key)
#         break


#확인용
print(type(mem), mem)