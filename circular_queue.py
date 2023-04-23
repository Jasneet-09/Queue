class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None for i in range(k)] 
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return
        elif (self.front == -1): 
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
            return True
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return
        elif (self.front == self.rear): 
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            return True
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.k
            return True
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        if (self.front == -1):
            return True
        return False

    def isFull(self) -> bool:
        if ((self.rear + 1) % self.k == self.front):
            return True
        return False       

