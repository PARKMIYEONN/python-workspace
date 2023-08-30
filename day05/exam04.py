class Dog:
    pass
dog = Dog()
print(type(dog))

class Car:
    def drive(self):    # self : java에서 this 같은 것.
                        # 어떤 객체가 나를 소환했는지 알아야 하기 때문에 반드시 처음에 오는 인자는 self여야 함.
        print('운전을 합니다')

c = Car()
c.drive()
print(f'type(Car) 판단 : {isinstance(c, Car)}')
print(f'type(Car) 판단 : {isinstance(10, Car)}')
print(f'type(Car) 판단 : {isinstance([10, 20, 30], Car)}')

l = [10, 20, 30]
print(l[0], l.__getitem__(0))

# isinstanc(10, int) 데이터의 타입이 맞는지 확인하기 위한 함수. type(10) == 'int'이런 식으로는 판단할 수 없음