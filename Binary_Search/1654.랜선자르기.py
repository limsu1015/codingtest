# # k = [7, 9, 12, 16]
#
#
#
#
#
#
#
# import  sys
# from itertools import count
#
# input = sys.stdin.readline
# k, n = map(int, input().split())
# length = []
# for i in range(k):
#     a = list(map(int, input().split()))
#     length.append(a)
# sorted_length = sorted(length)
#
# start, end= 0, len(sorted_length)-1
# while start <= end:
#     mid = (start + end) // 2
#     count = 0
#     for lengths in sorted_length:
#         count += lengths // mid
#
#     if count >= n:
#         result = mid
#         low = mid + 1
#     else:
#         high = mid - 1
# print(result)

# 입력 받기
k, n = map(int, input().split())

# 각 랜선의 길이를 입력받아 리스트에 저장
lengths = []
for _ in range(k):
    lengths.append(int(input()))

# 이진 탐색을 위한 범위 설정
low, high = 1, max(lengths)

# 이진 탐색
result = 0
while low <= high:
    mid = (low + high) // 2

    # lengths 리스트에서 각 랜선을 mid 길이로 잘랐을 때 나오는 랜선의 개수 합산
    count = 0
    for length in lengths:
        count += length // mid

    # 랜선 개수가 목표보다 많거나 같다면, 더 긴 길이 시도
    if count >= n:
        result = mid  # 가능한 최대 길이 갱신
        low = mid + 1
    # 랜선 개수가 목표보다 적다면, 길이 줄이기
    else:
        high = mid - 1

# 결과 출력
print(result)



