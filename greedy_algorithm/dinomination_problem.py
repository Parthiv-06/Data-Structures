def denomination(x,deno):
    res=[]
    for i in range(len(deno)-1,-1,-1):
        while deno[i]<=x:
            x-=deno[i]
            res.append(deno[i])
    return  res
deno=[1,2,5,10,20,50,100]
x=48
print(denomination(x,deno))
