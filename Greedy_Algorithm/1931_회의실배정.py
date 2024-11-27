# 입력 받기
import sys
input = sys.stdin.read
data = input().splitlines()

# 회의 수
N = int(data[0])

# 회의 리스트
meetings = []
for i in range(1, N + 1):
    start, end = map(int, data[i].split())
    meetings.append((start, end))

# 종료 시간 기준 정렬 (종료 시간이 같으면 시작 시간 기준 정렬)
meetings.sort(key=lambda x: (x[1], x[0]))

# 회의 선택
count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

# 결과 출력
print(count)
