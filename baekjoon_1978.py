x = int(input())

l = input().split()

sum = 0
def is_prime(x):
    p=1
    count = 0
    if (x == 1):
        return count
    while(1):
        p += 1
        if (x==p):
            count+=1
            break
        if (x%p==0):
            break
    return count
for i in range(0,x):
    sum += is_prime(int(l[i]))
print(sum)