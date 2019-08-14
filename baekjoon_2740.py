l = map(int,input().split())
check = len(l[0]) # 첫번째 리스트 길이
l2 = 0 # 첫번째 리스트 개수 채크를 위한 변수
answer = []
while 1:
    l1 = len(l[l2])
    if check != l1: # 첫번째 리스트 길이와 다를 시 break
        l1 -= 1 # l1는 첫번째 리스트의 마지막 위치
        break
    l2 += 1 # l2는 두번째 리스트의 첫번째 위치
    l1 += 1
if l[:l1] == l2: # 첫번째 리스트 개수와 두번째 리스트 길이 비교

    x = l[l2:].copy()
    y = l[:l2].copy()
    tool = len(l[:l1])
else:
    y = l[l2:].copy()
    x = l[:l2].copy()
    tool = len(l[:])
for i in range(0,len(y)):
    answer.append([])
    for j in range(0,len(x)):
        answer[i].append()
