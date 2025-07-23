def generate_paranthesis(n):
    res=[]
    def generation(openp,closep,s):
        if openp==closep and openp+closep==2*n:
            res.append(s)
        if openp<n:
            generation(openp+1,closep,s+"(")
        if closep<openp:
            generation(openp,closep+1,s+")")
    generation(0,0,"")
    return res
n=3
print(generate_paranthesis(n))