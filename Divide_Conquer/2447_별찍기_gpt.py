# 입력 받기
n = int(input("Enter the value of n: "))

# 별 그리기
result = [["*"] * n for _ in range(n)]

# 공백 패턴 채우기
size = n
while size > 1: # size가 1이 될 때까지 반복합니다. 즉, size가 1일 때는 더 이상 나눌 수 없으므로, 최종 패턴이 완성됩니다.
    for i in range(0, n, size):
        # i는 size 크기의 블록이 시작하는 행의 인덱스입니다.
        # i는 size 단위로 증가하므로, 전체 격자를 size x size 크기의 작은 블록으로 나눕니다.
        for j in range(0, n, size):
            # j는 size 크기의 블록이 시작하는 열의 인덱스입니다.
            # 이 두 반복문(i, j)을 통해 전체 격자를 size x size 크기의 블록으로 나누고, 각 블록에 대해 중앙 부분을 공백으로 채웁니다.
            for x in range(i + size // 3, i + 2 * (size // 3)):
                # x는 현재 size x size 블록의 중앙 부분을 담당하는 행 인덱스입니다
                # i + size // 3부터 i + 2 * (size // 3)까지를 순회하며, 가운데 부분에 공백을 넣을 행의 범위를 지정합니다.
                for y in range(j + size // 3, j + 2 * (size // 3)):
                    # y는 현재 size x size 블록의 중앙 부분을 담당하는 열 인덱스입니다.
                    # j + size // 3부터 j + 2 * (size // 3)까지를 순회하며, 가운데 부분에 공백을 넣을 열의 범위를 지정합니다.
                    result[x][y] = " "
    size //= 3

# 결과 출력
for row in result:
    print(*row)
