n = int(input())
count = 0
for i in range(n):
    command = input().strip()
    stack = []

    for char in command:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if not stack:
        count += 1
print(count)