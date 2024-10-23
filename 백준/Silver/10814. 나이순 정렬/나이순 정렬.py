N = int(input())  # 회원의 수 입력
members = []

for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))  # (나이, 이름) 형태로 리스트에 저장

# 나이순으로 정렬 (기본적으로 첫 번째 요소(나이)로 정렬됨)
members.sort(key=lambda x: x[0])
#lambda x: x[0]는 입력값 x에 대해 x[0]을 반환하는 함수입니다
# 결과 출력
for age, name in members:
    print(age, name)
