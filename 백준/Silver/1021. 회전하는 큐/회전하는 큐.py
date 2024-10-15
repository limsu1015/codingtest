from collections import deque

# 입력 받기
N, M = map(int, input().split())  # 큐의 크기 N, 뽑아야 할 숫자의 개수 M
targets = list(map(int, input().split()))  # 뽑아야 할 숫자들

# 1부터 N까지의 수가 들어있는 큐 생성
dq = deque(range(1, N + 1))

count = 0  # 회전 횟수 카운트

# 타겟 숫자를 하나씩 처리
for target in targets:
    # 타겟이 현재 큐의 몇 번째에 있는지 확인
    target_idx = dq.index(target)
    
    # 왼쪽으로 이동하는 것과 오른쪽으로 이동하는 것 중 더 적은 횟수를 선택
    if target_idx <= len(dq) // 2:
        # 왼쪽으로 회전하는 경우
        dq.rotate(-target_idx)
        count += target_idx
    else:
        # 오른쪽으로 회전하는 경우
        dq.rotate(len(dq) - target_idx)
        count += (len(dq) - target_idx)
    
    # 첫 번째 위치에서 타겟을 뽑아내고 제거
    dq.popleft()

# 결과 출력
print(count)
