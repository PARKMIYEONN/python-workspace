'''
    총사원수는 0명입니다
    Employee(10, 홍길동, 사원, 3000)
    Employee(20, 고길동, 사원, 3300)
    Employee(30, 한길동, 대리, 4000)
    Manager(100, 최길동, 부장, 7000)
    총사원수는 4명입니다
'''

class Employee:
    def __init__(self, **args):
        self.args = args

    def countEmployee(self):
        for e in self.args:
            print(e)

class Manager(Employee):
    def __init__(self, empList):





e1 = Employee(10, '홍길동', '사원', 3000)
e2 = Employee(20, '고길동', '사원', 3300)
e3 = Employee(30, '한길동', '대리', 4000)

Employee.countEmployee()