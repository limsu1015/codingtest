def solution(citations):
    answer = 0
    citations.sort()
    for i in range(0, len(citations)):
        if(citations[i] >= len(citations) - i):
            answer = max(answer, len(citations) - i)
    return answer