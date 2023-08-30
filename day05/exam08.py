class Person:

    #def __del__ 이용해서 줄어들때마다 어떤 작용을 하는 어쩌구 만들기
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.__addr = addr

    @property   #얘를 썼을 때 변수처럼 사용해도 getter가 호출되도록 할 수 있다
    def addr(self):
        return self.__addr
    # def getAddr(self):
    #     return self.__addr

    @addr.setter    # 변수명으로 setter메소드를 쓰는것처럼 만들어줄 수 있음.
    def addr(self, addr):
        self.__addr = addr

    def info(self):
        print(f'name : {self.name}, age : {self.age}, addr : {self.__addr}')



p = Person('홍길동', 25, '서울')
p.info()
print(p.name)
print(p.age)
# print(p.__addr)
# print(p.getAddr())
print(p.addr)

p.addr = '부산'
print(p.addr)