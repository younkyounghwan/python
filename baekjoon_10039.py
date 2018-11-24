sum = 0
for i in range(0,5):
    x = int(input())
    if x<40:
        x = 40
    sum += x
print(sum//5)