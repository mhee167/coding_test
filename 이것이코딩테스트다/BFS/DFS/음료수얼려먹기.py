#음료수 얼려먹기

N,M = map(int, input().split())
ice = [list(map(int,input())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited = [[False]*M for _ in range(N)]
ice_cream=0

def dfs(ice,x,y,visited):
    visited[x][y]=True
    
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue

        if ice[nx][ny]==0 and not visited[nx][ny]:
            dfs(ice,nx,ny,visited)
            
        

for i in range(N):
    for j in range(M):
        if ice[i][j]==0 and not visited[i][j]:
            dfs(ice,i,j,visited)
            ice_cream+=1


   