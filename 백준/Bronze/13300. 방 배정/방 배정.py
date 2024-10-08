n, k = map(int, input().split())
student = [[0] * 6 for i in range(2)]

for i in range(n):
    s, y = map(int, input().split())
    student[s][y-1] += 1

rooms = 0
for s in range(2):
    for y in range(6):
        if student[s][y] > 0:
            rooms += (student[s][y] +k -1 ) // k
print(rooms)