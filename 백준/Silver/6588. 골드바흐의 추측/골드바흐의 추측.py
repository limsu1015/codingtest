import sys
input = sys.stdin.readline

arr = [True] * 1000001
for i in range(2, 1001):
    if arr[i]:
        for j in range(i + i,1000001, i):
            arr[j] = False
while True:
    A = int(input())
    if A == 0:
        break
    for i in range(3,len(arr)):
        if arr[i] and arr[A-i]:
            print(A, "=", i, "+", A - i)
            break