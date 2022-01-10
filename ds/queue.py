class Queue:
    def __init__(self):
        self.queue = [];
    
    def front(self):
        if len(self.queue) == 0:
            return IndexError("empty")
        return self.queue[0]
    
    def end(self):
        if len(self.queue) == 0:
            return IndexError("empty")
        return self.queue[-1]
    
    def insert(self, value):
        self.queue.append(value)
        print(self.queue)
    
    def delete(self):
        if len(self.queue) == 0:
            return IndexError("empty")
        return self.queue.pop(0)

queue = Queue()
queue.insert(3)
queue.insert(5)
queue.insert(1)
queue.insert(10)
print(queue.delete())
print(queue.queue)