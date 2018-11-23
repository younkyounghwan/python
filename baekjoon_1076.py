l=[]
sum = ""
for i in range(0,3):
    x = input()
    l.append(x)
for i in range(0,2):
    if l[i] == "black":
        if i != 0:
            sum = sum + "0"
    elif l[i] == "brown":
        sum = sum + "1"
    elif l[i] == "red":
        sum = sum + "2"
    elif l[i] == "orange":
        sum = sum + "3"
    elif l[i] == "yellow":
        sum = sum + "4"
    elif l[i] == "green":
        sum = sum + "5"
    elif l[i] == "blue":
        sum = sum + "6"
    elif l[i] == "violet":
        sum = sum + "7"
    elif l[i] == "grey":
        sum = sum + "8"
    elif l[i] == "white":
        sum = sum + "9"

sum = int(sum)
if l[2] == "black":
    sum *= 1
elif l[2] == "brown":
    sum *= 10
elif l[2] == "red":
    sum *= 100
elif l[2] == "orange":
    sum *= 1000
elif l[2] == "yellow":
    sum *= 10000
elif l[2] == "green":
    sum *= 100000
elif l[2] == "blue":
    sum *= 1000000
elif l[2] == "violet":
    sum *= 10000000
elif l[2] == "grey":
    sum *= 100000000
elif l[2] == "white":
    sum *= 1000000000
print(sum)