def solution(numbers):
    answer = ''
    num_list = [] 

    for num in numbers:
        num_str = str(num)
        num_list.append((num_str * 3, len(num_str)))

    num_list.sort(reverse=True)

    total_sum = 0
    for n, l in num_list:
        total_sum += int(n[:l])
        if total_sum == 0: 
            return "0"
        answer += n[:l]
    return answer