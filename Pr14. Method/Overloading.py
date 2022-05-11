""" from tokenize import Name


class Emp:
    no_of_lever=8

    def __init__(self,name,asalary,arole):
        self.name = Name
        self.salary = asalary
        self.role =arole

 """

# 1)

    
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1+p2)


# 2)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(2, 3)
print(p1)
