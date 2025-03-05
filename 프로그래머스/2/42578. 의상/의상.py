def solution(clothes):
    ootd = {}
    for name, kind in clothes:
        if kind in ootd.keys():
            ootd[kind] += [name]
        else:
            ootd[kind] = [name]
    answer = 1
    for _, value in ootd.items():
        answer *= (len(value) + 1)
    
    return answer -1