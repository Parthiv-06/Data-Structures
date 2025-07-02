def asteroidCollision(asteroids):
    stack=[]
    for i in range(len(asteroids)):
        if asteroids[i]>0:
            stack.append(asteroids[i])
        else:
            while len(stack)!=0 and stack[-1]>0 and stack[-1]<-(asteroids[i]):
                stack.pop()
            if len(stack)!=0 and stack[-1]==-(asteroids[i]):
                stack.pop()
            elif len(stack)==0 and asteroids[i]<0 or stack[-1]<0 and asteroids[i]<0 :
                stack.append(asteroids[i])
    return stack
s=[4,7,1,-3,-7,17,15,-16]
print(asteroidCollision(s))