class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)
        while len(self.stack1):
            num = self.stack1.pop()
            self.stack2.append(num)
        while len(self.stack2):
            num = self.stack2.pop()
            self.stack1.append(num)
        

    def pop(self) -> int:
        while len(self.stack1):
            num = self.stack1.pop()
            self.stack2.append(num)
        answer = self.stack2.pop()
        while len(self.stack2):
            num = self.stack2.pop()
            self.stack1.append(num)
        return answer

    def peek(self) -> int:
        while len(self.stack1):
            num = self.stack1.pop()
            self.stack2.append(num)
        answer = self.stack2[-1]
        while len(self.stack2):
            num = self.stack2.pop()
            self.stack1.append(num)
        return answer
    
    
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()