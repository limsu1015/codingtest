# 0 1 2 3 4
# 1 3 2 1 4


import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
turn = 0
count = 0
for i in range(n):
    target = a[turn]
    count += 1
    if target == k:
        print(count)
        break
    turn = target
else:
    print(-1)
