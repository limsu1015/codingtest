import sys
input = sys.stdin.readline
n = int(input())
number = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if number[i][k] and number [k][j]:
                number[i][j] = 1

for row in number:
    print(*row)