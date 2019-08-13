l = map(int,input().split())
check = len(l[0]) # 첫번째 리스트 길이
l2 = 0 # 첫번째 리스트 개수 채크를 위한 변수

while 1:
    l1 = len(l[l2])
    if check != l1: # 첫번째 리스트 길이와 다를 시 break
        l1 -= 1 # l1는 첫번째 리스트의 마지막 위치
        break
    l2 += 1 # l2는 두번째 리스트의 첫번째 위치
    l1 += 1
if l[:l1] == len(l2): # 첫번째 리스트 개수와 두번째 리스트 길이 비교

    x = l[l2:].copy()
    y = l[:l2].copy()
for i in range(0,)
