
def gen(n):
    if n>0:
        for i in range(1,n+1):
            print()
            for j in range(1,i+1):
                print(j,end="")
        for r in range(n-1,0,-1):
            print()
            for k in range(1,r+1):
                print(k,end="")
    else:
        print("Enter a number above 0")
            

try:
    n=int(input())
    gen(n)
except ValueError:
    print("Enter a number")

