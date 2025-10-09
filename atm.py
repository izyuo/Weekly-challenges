try:
    cur=int(input())
except ValueError:
    print("iNVALID iNPUT")

t=0
f=0
h=0
rst=True

while cur!=0:
    if cur%2000==0:
        cur=cur-2000
        t=t+1
    elif cur%500==0:
        cur=cur-500
        f=f+1
    elif cur%100==0:
        cur=cur-100
        h=h+1
    else:
        rst=False
        break

if rst:
    print(f"2000 x {t}\n500 x {f}\n100 x {h}")
else:
    print("Invalid Amount")
