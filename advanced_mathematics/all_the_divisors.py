def all_the_divisors(n):
    st=set()
    for i in range(1,int(n**1/2)):
        if n%i==0:
            st.add(i)
            st.add(n//i)
    return st
n=36
print(all_the_divisors(n))