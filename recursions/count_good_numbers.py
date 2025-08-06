def count_good_nubmers(n):
    def countt(base,exp):
        res=1
        while exp>0:
            if exp%2==1:
                res=res*base
            base=base*base
            exp//=2
        return res
    even=(n+1)//2
    odd=n//2
    return countt(5,even)*countt(4,odd)
n=4
print(count_good_nubmers(n))