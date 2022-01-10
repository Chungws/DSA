class P_Queue:
    def __init__(self):
        self.heap = [];
        
    def parent_index(self, index):
        return (index-1)//2
    
    def left_child_index(self, index):
        return index*2 + 1
    
    def right_child_index(self, index):
        return index*2 + 2
    
    def swap(self, first, second):
        temp = self.heap[first]
        self.heap[first] = self.heap[second]
        self.heap[second] = temp
    
    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap)-1
        while index != 0 and self.heap[self.parent_index(index)] >= value:
            self.swap(self.parent_index(index), index)
            index = self.parent_index(index)
        print(self.heap)
                
    def delete(self):
        if len(self.heap) == 0:
            return IndexError("empty")
        self.swap(0, len(self.heap)-1)
        index = 0
        pop = self.heap.pop()
        while True:
            left, right = self.left_child_index(index), self.right_child_index(index)
            next = index
            if left < len(self.heap) and self.heap[left] < self.heap[next]:
                next = left
            if right < len(self.heap) and self.heap[right] < self.heap[next]:
                next = right
                
            if index == next:
                break
            
            self.swap(next, index)
            index = next
        print(self.heap)
        return pop

p_queue = P_Queue()
p_queue.insert(3)
p_queue.insert(5)
p_queue.insert(1)
p_queue.insert(10)
p_queue.insert(8)
p_queue.insert(7)
p_queue.insert(4)
p_queue.insert(5)
p_queue.insert(2)
p_queue.insert(6)
p_queue.insert(9)

print(p_queue.delete())

p_queue.insert(5)