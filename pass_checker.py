import re

pas=input()
rst=False


if len(pas)>=8:
    if re.search(r"[a-z]",pas):
        if re.search(r"[A-Z]",pas):
            if re.search(r"[0-9]",pas):
                checksp=any(not ch.isalnum() for ch in pas)
                if checksp:
                    rst=True

if rst:
    print("Strong password")
else:
    print("Weak password")