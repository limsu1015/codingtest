import sys
input = sys.stdin.readline

n = int(input())

result = [["*"] * n for _ in range(n)]

for i in range(0, n):
    for j in range(0, n):
