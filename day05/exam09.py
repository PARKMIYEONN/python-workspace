class Parent:
    def __init__(self):
        self.name = '부모'
        print('Parent() 호출...')
    def info(self):
        print('Parent info() 호출...')

class Child(Parent):    #Parent클래스를 상속받아서 자식 클래스를 만들었다
    def __init__(self):
        super().__init__()  #부모꺼 호출
        print('Child() 호출...')

    def info(self):
        super().info()
        print('Child info() 호출...')

# p = Parent()
# p.info()
p = Child()
p.info()
print(p.name)



