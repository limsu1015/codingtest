room_number = input()
digit_count = [0] * 10
for digit in room_number:
    digit_count[int(digit)] += 1

six_nine_count = (digit_count[6] + digit_count[9] + 1) // 2

digit_count[6] = six_nine_count
digit_count[9] = six_nine_count


print(max(digit_count))