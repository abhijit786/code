
class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b


c = Calculator(10,20)
print(c.sum())
