class meeting:
    def __init__(self,start,end,pos):
        self.start=start
        self.end=end
        self.pos=pos

def n_meetings_in_a_room(s,e):
    meet=[meeting(s[i],e[i],i+1)for i in range(len(s))]
    sorted(meet,key=lambda x:(x.end,x.pos))
    a_end=meet[0].end
    res=[]
    res.append(meet[0].pos)
    for i in range(1,len(s)):
        if a_end<meet[i].start:
            res.append(meet[i].pos)
            a_end=meet[i].end
    return res
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 5, 7, 9, 9]
print(n_meetings_in_a_room(start,end))


        