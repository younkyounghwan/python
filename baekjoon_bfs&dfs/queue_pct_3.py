import queue
q = queue.Queue(2)
q.put('a')
q.put('b') #큐의 저장 한계
# q.put('c') #다른 스레드가 아이쳄을 가지고 갈 때까지 무한 대기


p = queue.Queue(2)
p.put_nowait('a')
p.put_nowait('b')
# p.put_nowait('c') # 큐 객체가 꽉찬 경우

print(p.get_nowait())
print(p.get_nowait())

r = queue.Queue(2)
r.put('a')
r.put('b')
r.put('c', True,5) #5초동안 대기 후 블로킹 됨

r.put('c', False) # 다음과 같이 작성 시 put_nowait()과 동일한 동작을 수행함.