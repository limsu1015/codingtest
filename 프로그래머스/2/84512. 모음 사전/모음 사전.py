from itertools import product

def solution(word):
    alpha = ["A", "E", "I", "O", "U"]
    dictionary = []
    
    # 길이가 1~5인 모든 단어 조합 생성
    for length in range(1, 6):  # 1~5 길이의 단어 생성
        for order in product(alpha, repeat=length):  
            dictionary.append(''.join(order))  # 튜플을 문자열로 변환하여 추가

    dictionary.sort()  # 사전 순 정렬
    return dictionary.index(word) + 1  # 단어의 인덱스 +1 반환