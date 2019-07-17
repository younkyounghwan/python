from  math import factorial
x, y = map(int,input().split())
c = int(factorial(x)//(factorial(y)*factorial(x-y)))
print("%d" %(c%10007))