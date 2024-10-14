from collections import deque
import sys
input = sys.stdin.read

queue = deque()
commands = input().splitlines()

n = int(commands[0])  # 명령어의 개수

for i in range(1, n+1):
    command = commands[i].split()
    
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if not queue else 0)
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
