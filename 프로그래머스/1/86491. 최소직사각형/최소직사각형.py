def solution(sizes):
    a = len(sizes)
    w = 0
    h = 0
    
    for i in range(a):
        sizes[i].sort()
        w = max(w, sizes[i][0])
        h = max(h, sizes[i][1])
    answer = w * h
    return answer