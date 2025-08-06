def generate_all_the_binary_strings(n):
    res=[]
    s=""
    def generation(s,n):
        if len(s)==n:
            res.append(s)
            return 
        generation(s+"0",n)
        generation(s+"1",n)
    generation(s,n)
    return res
print(generate_all_the_binary_strings(3))
