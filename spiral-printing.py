
n = int(input("Enter no:"))


matrix = [[0]*n for _ in range(n)]


def clockwise(matrix):
    num = 1
    top, left = 0, 0
    bottom, right = n-1, n-1
    while left<=right and top<=bottom:
        #left--->right
        for i in range(left,right+1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Top ---> bottom
        for i in range(top,bottom+1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # right ----> left
        if top<=bottom:
            for i in range(right,left-1,-1):
                matrix[bottom][i]=num
                num+= 1
            bottom-= 1

        # bottom ------> top
        if left<=right:
            for i in range(bottom,top-1,-1):
                matrix[i][left]=num
                num+= 1
            left+= 1
    return matrix

def anti_clockwise(matrix):
    num = 1
    top, left = 0, 0
    bottom, right = n-1, n-1
    while left<=right and top<=bottom:
        for i in range(top,bottom+1):  #0,4
            matrix[i][left]=num
            num+=1
        left+=1

        for i in range(left,right+1): # 1,4
            matrix[bottom][i]=num
            num+=1
        bottom-=1

        if left<=right:
            for i in range(bottom,top-1,-1):
                matrix[i][right]=num
                num+=1
            right-=1

        if top<=bottom:
            for i in range(right,left-1,-1):
                matrix[top][i]=num
                num+=1
            top+=1
    return matrix


def prnt(result):
    for i in result:
            for j in i:
                print(f"{j:3}",end=" ")
            print()



print("\n 1. Clockwise\n2. Anti-clockwise")

try:
    choice=int(input("Enter your choice: "))
    if choice==1:
        rst=clockwise(matrix)
        prnt(rst)

    elif choice==2:
        rst=anti_clockwise(matrix)
        prnt(rst)

    else:
        print("Enter a valid Choice")
except ValueError:
    print("Enter numbers only")
