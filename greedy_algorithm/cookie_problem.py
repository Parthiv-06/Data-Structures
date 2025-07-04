def cookie(greed,s):
    greed.sort()
    s.sort()
    l,r,cnt=0,0,0
    while r<len(s) and l<len(greed):
        if greed[l]<=s[r]:
            cnt+=1
            l+=1
            r+=1
        else:
            r+=1
    return cnt
greed=[1,2,3]
s=[1,1]
print(cookie(greed,s))