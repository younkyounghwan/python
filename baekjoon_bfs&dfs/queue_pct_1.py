import queue

q=queue.Queue()

q.put('apple') #큐 객체에 데이터 입력

q.put('banana')

q.put(10)

print(q.qsize()) #큐 객체에 저장된 데이터 갯수

print(q.get()) #큐 객체에서 데이터 출력

print(q.get())

print(q.qsize()) #2개 출력후 저장된 데이터 갯수

