given = input("Enter string: ")

stack = []
found = False 

for bck in given:
    if bck in "{[(":
        stack.append(bck)
        found = True
    elif bck in "}])":
        found = True
        if not stack:
            print("Not Balanced")
            break
        top = stack.pop()
        if (bck == ')' and top != '(') or \
           (bck == ']' and top != '[') or \
           (bck == '}' and top != '{'):
            print("Not Balanced")
            break
else:
    if not found:
        print("No brackets given")
    elif not stack:
        print("Balanced")
    else:
        print("Not Balanced")








