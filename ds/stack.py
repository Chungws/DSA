class Stack:
    def __init__(self):
        self.stack = [];
    
    def top(self):
        if len(self.stack) == 0:
            return IndexError("empty")
        return self.stack[-1]
    
    def insert(self, value):
        self.stack.append(value)
        print(self.stack)
    
    def delete(self):
        if len(self.stack) == 0:
            return IndexError("empty")
        return self.stack.pop()

stack = Stack()
stack.insert(3)
stack.insert(5)
stack.insert(1)
stack.insert(10)
print(stack.delete())
print(stack.stack)