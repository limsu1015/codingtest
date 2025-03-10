import sys
import bisect

input = sys.stdin.read().split()
index = 0
T = int(input[index])  # 테스트 케이스 개수
index += 1
results = []

for _ in range(T):
    # 배열 크기 읽기
    a, b = map(int, (input[index], input[index + 1]))
    index += 2
    
    # 배열 A, B 읽고 정렬
    arrA = sorted(map(int, input[index : index + a]))
    arrB = sorted(map(int, input[index + a : index + a + b]))
    index += a + b
    
    # 이분 탐색을 이용한 비교
    count = 0
    for num in arrA:
        count += bisect.bisect_left(arrB, num)
    
    results.append(str(count))

sys.stdout.write("\n".join(results) + "\n")