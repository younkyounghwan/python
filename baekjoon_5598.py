s = input()
s1 = ""
for i in range(len(s)):
    if s[i] == "A":
        s1 += "X"
    elif s[i] == "B":
        s1 += "Y"
    elif s[i] == "C":
        s1 += "Z"
    else:
        s1 += chr(ord(s[i])-3)
print(s1)