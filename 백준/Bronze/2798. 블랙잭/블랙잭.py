N, M = map(int, input().split())  # 카드 개수 N, 목표 합 M
cards = list(map(int, input().split()))  # 카드 리스트

max_sum = 0  # M을 넘지 않는 최대 합

# 3중 반복문으로 3장의 카드를 선택
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            card_sum = cards[i] + cards[j] + cards[k]  # 3장의 카드 합
            # 합이 M을 넘지 않으면서, 현재까지 가장 큰 값을 저장
            if card_sum <= M:
                max_sum = max(max_sum, card_sum)

# 결과 출력
print(max_sum)