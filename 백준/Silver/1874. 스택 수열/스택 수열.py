n = int(input())  # 수열의 길이 입력
sequence = [int(input()) for _ in range(n)]  # 수열 입력

stack = []  # 스택
result = []  # 결과 저장 (push와 pop 연산을 저장할 리스트)
current = 1  # 스택에 넣을 숫자
possible = True  # 수열을 만들 수 있는지 여부

for num in sequence:
    # 스택에 들어가야 할 숫자가 num에 도달할 때까지 push
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 스택의 최상단이 num과 같으면 pop
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

# 수열을 만들 수 있으면 연산 순서 출력, 아니면 NO 출력
if possible:
    print('\n'.join(result))
else:
    print("NO")
