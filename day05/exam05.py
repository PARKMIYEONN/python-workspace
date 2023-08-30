class TV:
    def __init__(self):     #객체 생성 시 한 번 호출되며, 주로 객체의 초기 속성을 설정하는 용도로 사용됩니다.
        # print('초기화 진행')
        self.power = False  # 클래스 내에서의 self변수를 써주면 public한 멤버변수처럼 쓸 수 있다
        self.channel = 10

    def info(self):         #이 메서드를 호출하려면 이미 객체가 생성되어야 합니다.
        print(f'채널정보 : {self.channel}')
        if 'volume' in self.__dict__:   # 호출한 객체에 volume 변수가 있을 때에만 밑에 있는 기능을 실행
            print(f'음량정보 : {self.volume}')

tv = TV()
print(tv.power)
tv.info()
tv.volume = 20  # 표준화된 변수가 아님. 특정 객체에 일부 특징을 마음대로 추가할 수 있음
print(tv.volume)
tv.info()

class Car:
    def __init__(self, name, price):    # 첫 인자는 무조건 self 그 뒤에 인자를 추가해야 함
        self.name = name
        self.price = price

    def info(self):
        print(f'자동차명 : {self.name}\t가격 : {self.price}')

c = Car('그랜저', 4000)
c2 = Car('모닝', 2100)
c.info()
c2.info()