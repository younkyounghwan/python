import queue

def GetItemList(q): #큐 객체의 데이터 출력용 함수
    ret=[]
    n=q.qsize()
    while n > 0:
        ret.append(q.get())
        n -= 1
    return ret


#선입선출 : first - in, first - out
l = 'apple,banana,orange'
q = queue.Queue()
for i in l.split(','):
    q.put(i)
print(GetItemList(q))

#후입선출 : last - in, first - out
l = 'apple,banana,orange'
q = queue.LifoQueue()
for i in l.split(','):
    q.put(i)
print(GetItemList(q))