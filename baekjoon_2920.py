x = input().split()
for i in range(0,8):
    x[i] = int(x[i])
l = [1,2,3,4,5,6,7,8]
d = [8,7,6,5,4,3,2,1]
if x == l:
    print("ascending")
elif x == d:
    print("descending")
else:
    print("mixed")
