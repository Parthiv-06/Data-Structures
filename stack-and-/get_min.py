class stack:
    def __init__(self):
        self.st=[]
    def push(self,val):
        min_val=self.get_min()
        if min_val is None or min_val>val:
            min_val=val
        self.st.append([val,min_val])
    def pop(self):
        self.st.pop()
    def top_el(self):
        return self.st[-1][0] if self.st else None
    def get_min(self):
        return self.st[-1][1] if self.st else None
s=stack()
s.push(10)
s.push(12)
s.push(8)
print(s.get_min())
s.pop()
print(s.get_min())