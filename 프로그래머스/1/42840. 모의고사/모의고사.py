def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [ 0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            scores[0] += 1
        if answers[i] == b[i % len(b)]:
            scores[1] += 1
        if answers[i] == c[i % len(c)]:
            scores[2] += 1
    
    max_score = max(scores)
    
    answer = []
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)
    return answer