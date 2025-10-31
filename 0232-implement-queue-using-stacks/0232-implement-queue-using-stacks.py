from queue import LifoQueue
class MyQueue:

    def __init__(self):
        self.inp=LifoQueue()
        self.op=LifoQueue()

    def push(self, x: int) -> None:
        self.inp.put(x)
        

    def pop(self) -> int:
        if self.op.empty():
            while not self.inp.empty():
                self.op.put(self.inp.get())
        x=self.op.get()
        return x
        

    def peek(self) -> int:
        if self.op.empty():
            while not self.inp.empty():
                self.op.put(self.inp.get())
        return self.op.queue[-1]
        

    def empty(self) -> bool:
        return not self.inp.qsize()+self.op.qsize()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()