class MyQueue:
    def __init__(self):
        self.data = []     
        self.front = -1
        self.rear = -1 

    def push(self, x: int) -> None:
        self.data.append(x)
        self.rear += 1
        if self.front == -1:
            self.front=0

    def pop(self) -> int:
        if self.empty():
            return
        else:
            x = self.data.pop(0)
            self.front += 1
            return x


    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        if len(self.data)==0:
            return True
        return False
        
