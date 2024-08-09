class Employee:
    id = 0
    def __init__(self, name):
        self.name = name
        Employee.id += 1

    def __str__(self):
        return "사번: {}, 이름: {}".format(self.id,self.name)

emp1 = Employee("최사원")
print(emp1)