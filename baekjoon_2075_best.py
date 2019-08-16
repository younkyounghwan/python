n=int(input())
a=[]
for _ in[0]*n:
    a+=map(int,input().split());
    a.sort();
    a[:-n]=() # 유효값 제시
print(a[0])

