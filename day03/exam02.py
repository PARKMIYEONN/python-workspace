'''
range형의 데이터는 연산이 안 됨. range끼리 더한다고 그게 합쳐지거나 하지 않음

key, value 쌍을 갖는 것을 dictionary? 라고 함
'''

data = {'hong': 1111, 'kang': 2222, 'han': 3333, 'park': 4444, 'kang': 5555}
                                # key값은 중복될 수 없음. 같은 값이 들어있으면 뒤에 나온 값으로 업데이트 되어서 들어감
print(data, type(data))

stuInfo = {'name': 'hong', 'age': 28, 'scores': [100, 100, 70]}
                                # dictionary안에 value는 여러 형태가 가능. 그 안에 또 list형태를 넣는 것도 가능하다
print(stuInfo)

data = {}
print(data, type(data))
data = dict()
# data = dict(key=value, key=value) 형태로 생성 가능, 이 형태는 key가 문자열인 형태만 가능하다
data = dict(name='hong', age=28, addr='seoul')
data = dict([('name', 'hong'), ('age', 28), ('addr', 'seoul'), (100, 'max')]) #key value를 튜플의 형태로 넣어줌
                                                                    #이 형태로는 key값에 정수형태도 넣을 수 있다
data = dict(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))

print(data, type(data))

print(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))  # zip객체

