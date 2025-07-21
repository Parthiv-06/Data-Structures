def string_palindrome_check(s,n,i):
    if i>=n//2:
        return True
    if s[n-i-1]==s[i]:
        return string_palindrome_check(s,n,i+1)
    else:
        return False
s="MADAM1"
print(string_palindrome_check(s,6,0))
