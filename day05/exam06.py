class Car:
    def __init__(self, **args):
        self.args = args

    def info(self):
        for key, value in self.args.items():
            print(f'{key} : {value}')
        print('=' * 20)

class Car:
    addr = '서울' # 이런식으로 멤버변수를 만들면 static처럼 하나만 만들어지는 것. 클래스명.addr이런 식으로 접근함
    __slots__ = ['name', 'price', 'company']    # 해당 클래스가 가질 수 있는 멤버변수를 미리 정함
    def __init__(self, **args):
        if 'name' in args:
            self.name = args['name']
        if 'price' in args:
            self.price = args.get('price')
        if 'company' in args:
            self.company = args.get('company')
            Car.addr='부산'   #company가 있을때라는 조건이 걸려있어서 c1만 바뀔 것 같지만
                             #하나의 변수를 공유하고 있어서 하나가 바뀌면 두개가 같이 바뀜

    def info(self):
        print(f'{self.name}의\t가격은 {self.price}만원')

c = Car(name='그랜저', price=4000, company='현대')
c2 = Car(name='모닝', price=2100)
c.info()
c2.info()
print(c.addr)
print(c2.addr)

print(c.addr)
print(c2.addr)