# 테스트 케이스의 개수 입력
t = int(input())

for _ in range(t):
    data = input().strip()
    
    left_stack = []
    right_stack = []
    
    for char in data:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())  # 왼쪽에서 오른쪽으로 이동
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())  # 오른쪽에서 왼쪽으로 이동
        elif char == '-':
            if left_stack:
                left_stack.pop()  # 왼쪽에서 문자 삭제
        else:
            left_stack.append(char)  # 문자 삽입
    
    # 결과 출력 (left_stack + right_stack[::-1])
    print(''.join(left_stack + list(reversed(right_stack))))
