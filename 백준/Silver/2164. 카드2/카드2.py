# n = int(input())
# q = list(range(1, n+1))
# while len(q) > 1:
#     q.pop(0)
#     q.append(q.pop(0))
# print(q[0])
# 내코드

from collections import deque

n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
    queue.popleft() 
    queue.append(queue.popleft())
print(queue[0])
#지피티코드