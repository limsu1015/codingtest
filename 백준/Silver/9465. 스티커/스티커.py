import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())  # 스티커 열의 개수
    top = list(map(int, input().split()))  # 위쪽 스티커 점수
    bottom = list(map(int, input().split()))  # 아래쪽 스티커 점수

    if n == 1:
        # 열이 하나면 둘 중 큰 값을 출력
        print(max(top[0], bottom[0]))
        continue

    # 초기값 설정
    prev_top = top[0]  # dp[0][0]
    prev_bottom = bottom[0]  # dp[1][0]
    curr_top = top[1] + bottom[0]  # dp[0][1]
    curr_bottom = bottom[1] + top[0]  # dp[1][1]

    # DP 점화식 적용
    for i in range(2, n):
        new_top = top[i] + max(curr_bottom, prev_bottom)  # dp[0][i]
        new_bottom = bottom[i] + max(curr_top, prev_top)  # dp[1][i]
        # 갱신
        prev_top, prev_bottom = curr_top, curr_bottom
        curr_top, curr_bottom = new_top, new_bottom

    # 최댓값 출력
    print(max(curr_top, curr_bottom))
