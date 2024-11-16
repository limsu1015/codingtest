import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] > a[i]:  # 감소 조건
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
