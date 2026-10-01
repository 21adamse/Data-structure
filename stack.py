class Stack():
    def __init__(self,limit):
        self.list = []
        self.limit = limit
    def push(self,data):
        if len(self.list) < self.limit:
            self.list.append(data)
            print("Data pushed")
        else:
            print("Stack full")
    def pop(self):
        if len(self.list) > 0:
            print("Data popped-",self.list.pop())
        else:
            print("No data in stack")
    def numvalues(self):
        print("Number of values in stack-",len(self.list))
    def display(self):
        if len(self.list) > 0:
            print("Values in stack:")
            for value in self.list:
                print(value,end=" ")
            print("")
        else:
            print("No values in stack")

numberstack = Stack(5)
numberstack.push(55)
numberstack.push(25)
numberstack.push(35)
numberstack.push(45)
numberstack.push(15)
numberstack.push(65)
numberstack.display()
numberstack.pop()
numberstack.pop()
numberstack.pop()
numberstack.pop()
numberstack.display()
numberstack.pop()
numberstack.pop()
numberstack.numvalues()
numberstack.display()