class stack:
    def __init__(self):
        self.top=-1
        self.size=100
        self.arr=[0]*self.size
    def  push(self,x):
        self.top+=1
        self.arr[self.top]=x
    def pop(self):
        x=self.arr[self.top]
        self.top-=1
        return x
    def size_stack(self):
        return self.top+1
    def top_el(self):
        return self.arr[self.top]
    
if __name__=="__main__":
    s=stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    print(s.pop())
    print(s.top_el())
    print(s.size_stack())