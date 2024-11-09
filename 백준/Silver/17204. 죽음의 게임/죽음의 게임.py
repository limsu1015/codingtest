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