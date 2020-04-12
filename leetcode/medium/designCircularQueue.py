# 622. Design Circular Queue

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.items = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.items) == self.size:
            return False
        self.items.append(value)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if len(self.items):
            del(self.items[0])
            return True
        return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if len(self.items):
            return self.items[0]
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if len(self.items):
            return self.items[-1]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if len(self.items) < 1:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if len(self.items) == self.size:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
param_1 = obj.enQueue(5)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()