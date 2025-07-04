def valid_paranthesis(s):
    min,max=0,0
    for i in range(len(s)):
        if s[i]=="(":
            min+=1
            max+=1
        elif s[i]==")":
            min-=1
            max-=1
        else:
            min-=1
            max+=1
        if min<0:
            min=0
        if max<0:
            return False
    if min==0:
        return True
    else:
        return False
s="())"
print(valid_paranthesis(s))