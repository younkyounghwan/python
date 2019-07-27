l = list(map(int,input().split()))
l.remove(max(l))
print(min(l)*max(l))