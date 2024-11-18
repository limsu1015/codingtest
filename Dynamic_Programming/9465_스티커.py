# 2    t = int(input())
# 5    n = int(input())
# 50 10 100 20 40 dp.append(list(map(int, input().split())))
# 30 50 70 10 60  dp.append(list(map(int, input().split())))
# 7    n = int(input())
# 10 30 10 50 100 20 40  dp.append(list(map(int, input().split())))
# 20 40 30 50 60 20 80   dp.append(list(map(int, input().split())))

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):   # 2
    n = int(input())   # 0: 5   1:  7
    dp = []
    for i in range(2):
        dp.append(list(map(int, input().split())))

    if n == 1:
        print(*max(dp))
    elif n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for i in range(2, n):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))





