def jump_game(a):
    max_jump=0
    for i in range(len(a)):
        if i >max_jump:
            return False
        max_jump=max(max_jump,i+a[i])
    return True
arr=[3,2,2,0,5]
print(jump_game(arr))