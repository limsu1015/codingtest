def solution(numbers):
    answer = ''
    list = [((str(num)*3),len(str(num))) for num in numbers]
    list.sort(reverse=True)
    
    sum = 0
    for n,l in list :
        sum += int(n[:l])
        if ( sum == 0):
            answer = "0"
            break
        else :
            answer += n[:l]
    return answer