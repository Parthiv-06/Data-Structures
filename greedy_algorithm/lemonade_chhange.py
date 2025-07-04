def lemonade_change(denominatin):
    fives,tens=0,0
    for i in range(len(denominatin)):
        if denominatin[i]==5:
            fives+=1
        elif denominatin[i]==10:
            if fives>0:
                fives-=1
            else:
                return False
            tens+=1
        else:
            if fives>2:
                fives-=3
            elif tens>0 and fives>0:
                fives-=1
                tens-=1
            else:
                return False
    return True
arr=[5,5,5,10,20]
print(lemonade_change(arr))