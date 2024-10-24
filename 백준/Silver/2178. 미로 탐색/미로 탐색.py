from collections import deque

# BFS 함수 정의
def bfs(x, y):
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()  # 큐에서 현재 위치를 꺼냄
        
        # 상하좌우로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위 안에 있어야 하고, 이동할 수 있는 칸(1)이어야 함
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                # 처음 방문하는 칸에 대해 최단 거리 기록
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))  # 큐에 새로운 위치를 추가
    
    # 가장 오른쪽 아래까지의 이동 거리 반환
    return maze[N-1][M-1]

# 입력 처리
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# BFS 수행 및 결과 출력
print(bfs(0, 0))
