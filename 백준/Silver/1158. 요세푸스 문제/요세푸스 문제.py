N, K = map(int, input().split())

# 사람 리스트 초기화
people = list(range(1, N + 1))

result = []  # 요세푸스 순열을 담을 리스트
index = 0    # 현재 제거할 인덱스

# 리스트에서 사람을 제거하면서 순열 생성
while people:
    index = (index + K - 1) % len(people)  # K번째 사람을 가리키는 인덱스 계산
    result.append(people.pop(index))       # 해당 인덱스의 사람을 제거하고 결과에 추가

# 결과를 원하는 형식으로 출력
print("<", ", ".join(map(str, result)), ">", sep="")