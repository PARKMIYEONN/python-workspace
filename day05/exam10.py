from abc import *
class TV(metaclass=ABCMeta):     #추상클래스로 만들 수 있음
    @abstractmethod  # 파이썬은 얘를 데코레이터라고 부름
    def power_on(self):
        pass

class LGTV(TV):
    def power_on(self):
        print('power ON...')

tv = LGTV()
tv.power_on()