# def removeKdigits(num,k):
#     stack = []

#     for digit in num:
#         while stack and k > 0 and stack[-1] > digit:
#             stack.pop()
#             k -= 1
#         stack.append(digit)

#     # If k > 0, remove remaining k digits from the end of the stack
#     stack = stack[:-k] if k > 0 else stack

#     # Remove leading zeros
#     result = ''.join(stack).lstrip('0')

#     # Handle edge case where result might be empty
#     return result if result else '0'
# num="1432219"
# k=3
# print(removeKdigits(num,k))

def removek(s,k):
    stack=[]
    for digits in s:
        while stack and k>0 and stack[-1]>digits:
            stack.pop()
            k-=1
        stack.append(digits)
    stack=stack[:-k] if k<0 else stack
    res=''.join(stack).lstrip('0')
    return res if res else '0'
s="1432219"
k=3
print(removek(s,k))