##큐객체(queue모듈에서 제공되는 3개의 클래스를 지칭)

# queue.Queue(maxsize)
# 선입선출(FIFO First-In, First-Out)큐 객체를 생성

# queue.LifoQueue(maxsize)
# 일반적으로 스택(Stack)이라 불리는 후입선출(LIFO Last-In, First-Out)큐 객체를 생성

# queue.PriorityQueue(maxsize)
# 우선순위 큐 객체를 생성 입력되는 아이템의 형식은 (순위, 아이템)의 튜플로 입력되며,
# 우선순위는 숫자가 작을수록 높은 순위를 갖는다.






## 위의 3개의 클래스는 아래표에 있는 메서드를 동일하게 가지고 있다.
# 각 메서드의 의미는 동일하지만, 해당 클래스의 정렬방식에 따라서 GET계열 메서드의 결과가 달라진다.

# qsize()
# 큐 객체에 입력된 아이템의 개수를 반환

# put(item[, block[, timeout]])
# 큐 객체에 아이템을 입력한다.

# put_nowait(item)
# 블로킹(blocking)없이 큐 객체에 아이템을 입력한다.
# 큐 객체가 꽉 차 있는 경우에는 queue.Full예외 발생

# get([block[, timeout]])
# 생성된 큐 객체 특성에 맞추어, 아이템 1개를 반환

# get_nowait()
# 블로킹(blocking)없이 큐 객체에 들어있는 아이템을 반환
# 큐 객체에 아이템이 없는 경우에는 queue.Empty 예외 발생





## 아래의 예외는 큐객체의 크기와 관련하여 발생할수 있는 예외이다

# queue.Empty
# 큐 객체에 아이템이 없는 경우 발생

# queue.Full
# 큐 객체에 아이템이 꽉 찬 경우에 발생

import queue

def GetItemList(q): #큐 객체의 데이터 출력용 함수
    ret=[]
    n=q.qsize()
    while n > 0:
        ret.append(q.get())
        n -= 1
    return ret

q = queue.Queue()
q.put('apple') #큐 객체에 데이터 입력
q.put('banana')
q.put(10)
print(q.qsize()) #큐 객체에 저장된 데이터 갯수
print(q.get()) #큐 객체에서 데이터 출력
print(q.get())
print(q.qsize()) #2개 출력후 저장된 데이터 갯수
