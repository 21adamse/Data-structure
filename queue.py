class Queue():
    def __init__(self,limit):
        self.list = [None]*5
        self.head = -1
        self.tail = -1
        self.limit = limit
    def enqueue(self,data):
        if (self.tail+1)%self.limit == self.head:
            print("Queue full")
            return 
        if self.head == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail+1)%self.limit
        self.list[self.tail] = data
    def dequeue(self):
        if self.head == -1:
           print("Queue empty")
           return
        dvalue = self.list[self.head]
        self.list[self.head] = None
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head+1)%self.limit
        print(dvalue,"removed from queue")
    def display(self):
        if len(self.list) > 0:
            print(self.list)
        else:
            print("Queue empty")
    def headtail(self):
        print("Current head position-",self.head)
        print("Current tail position-",self.tail)
    def numvalues(self):
        if len(self.list) > 0:
            print("There are",len(self.list),"values in the queue")
        else:
            print("Queue empty")

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()
queue.enqueue()
queue.enqueue()
queue.enqueue()
queue.enqueue()
queue.enqueue()


