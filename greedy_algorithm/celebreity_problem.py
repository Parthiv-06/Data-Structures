def celebrity(matrix):
    top=0
    bottom=len(matrix)-1
    while top<bottom:
        if matrix[top][bottom]==1:
            top+=1
        elif matrix[bottom][top]==1:
            bottom-=1
        else:
            top+=1
            bottom-=1
    if top>bottom:
        return -1
    else:
        return top
matrix=[[0,1,1,0],[0,0,0,0],[0,1,0,0],[1,1,0,0]]
print(celebrity(matrix))

