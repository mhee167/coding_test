from collections import deque

N, M = map(int, input().split())
maze = [list(map(int,input())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작점을 튜플로 올바르게 초기화
queue = deque([(0, 0)])
visited[0][0]=True


while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 미로 범위를 벗어나면 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        # 벽(0)이면 무시
        if maze[nx][ny] == 0:
            continue
        
        # 처음 방문하는 길(1)이면 
        if maze[nx][ny] == 1 and not visited[nx][ny]:
            # 이전 위치의 거리 + 1을 저장
            maze[nx][ny] = maze[x][y] + 1
            visited[nx][ny]=True
            queue.append((nx, ny))

result = maze[N-1][M-1]
print(result)