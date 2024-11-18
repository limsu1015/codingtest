import sys
input = sys.stdin.read
data = input().split()

# 입력 처리
t = int(data[0])
index = 1

results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    sticker = [list(map(int, data[index:index+n])), 
               list(map(int, data[index+n:index+2*n]))]
    index += 2 * n

    if n == 1:  # 열이 하나인 경우
        results.append(max(sticker[0][0], sticker[1][0]))
        continue

    # DP 배열 초기화
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[1][0] + sticker[0][1]
    dp[1][1] = sticker[0][0] + sticker[1][1]

    # DP 점화식
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

    # 최댓값 저장
    results.append(max(dp[0][n-1], dp[1][n-1]))

# 결과 출력
sys.stdout.write("\n".join(map(str, results)) + "\n")
