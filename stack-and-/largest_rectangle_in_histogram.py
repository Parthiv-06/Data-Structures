def largest_rectangle_in_histogram(h):
    stack=[]
    max_rec=0
    for i in range(len(h)):
        while stack and h[stack[-1]]>h[i]:
            el=stack[-1]
            stack.pop()
            next_el=i
            prev_el=stack[-1] if stack else -1
            max_rec=max(max_rec,h[el]*(next_el-prev_el-1))
        stack.append(i)
    return max_rec
s=[2,1,5,6,2,3,1]
print(largest_rectangle_in_histogram(s))