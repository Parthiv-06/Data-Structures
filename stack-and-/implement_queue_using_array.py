class Queue:
    def __init__(self):
        self.start=-1
        self.end=-1
        self.current_size=0
        self.max_size=16
        self.arr=[0]*self.max_size
    def push(self,el)->int:
        if self.current_size==self.max_size:
            print("queue is full: ")
            exit(1)
        if self.end==-1:
            self.start=0
            self.end=0
        else:
            self.end=(self.end+1)%self.max_size
        self.arr[self.end]=el
        print("pushed:",self.arr[self.end])
        self.current_size+=1
    def pop(self):
        if self.end==1:
            print("queue is empty: ")
            exit(1)
        popped=self.arr[self.start]
        if self.current_size==1:
            self.start=-1
            self.end=-1
        else:
            self.start=(self.start+1)%self.max_size
        print("popped element is : ",popped)
        self.current_size-=1
    def size_qu(self):
        print("current size of the queue is : ",self.current_size)
    def top_el(self):
        print("top element is queue is : ",self.arr[self.start])
if __name__=="__main__":
    q=Queue()
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)

    q.pop()
    q.pop()
    q.top_el()
    q.size_qu()