n = int(input())  # 탑의 개수
heights = list(map(int, input().split()))  # 탑의 높이 입력

stack = []
result = []

for i in range(n):
    while stack and stack[-1][1] < heights[i]:
        stack.pop()  # 현재 탑보다 낮은 탑들은 pop

    if stack:
        result.append(stack[-1][0] + 1)  # 수신 가능한 탑의 번호 저장 (1-based index)
    else:
        result.append(0)  # 수신할 수 있는 탑이 없으면 0 추가

    stack.append((i, heights[i]))  # 현재 탑의 인덱스와 높이 스택에 추가

print(' '.join(map(str, result)))
