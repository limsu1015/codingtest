# 0 1 2 3 4
# 1 3 2 1 4


import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
turn = 0 # 0번부터  지목 시작
count = 0 # 지목 횟수
for i in range(n):
    target = a[turn] # 첫 턴은 무조건 0번 부터 지목한 사람 (a의 0번 인덱스 시작)
    count += 1
    if target == k:
        print(count)
        break
    turn = target # a[0]의 인덱스 1로 위에 target = a[1]로 돌아가서 if문 만족할때까지 반복
else:
    print(-1)
