def bfs(N, M): # N 행, M 열
    visited = [[0]*M for _ in range(N)] # visited 생성
    q = [0]*(N*M) # 큐 생성
    front = -1
    rear = -1
    cnt = 0 # 안읻은 토마토 개수

    for i in range(N): # 시작점 인큐 ( 익은 토마토 위치)
        for j in range(M):
            if tomato[i][j]==1:
                rear += 1
                q[rear] = (i, j) # q.append(i, j)
                visited[i][j] = 1       # 시작점 인큐표시
            elif tomato[i][j] == 0:
                cnt += 1
    if cnt == 0 and len(q)>0:
        return 0 # 익은 토마토만 주어진 경우우

   while front != rear: # 큐가 비어있지 않으면
        # i, j = q.pop(0) # dledmsxhakxh
        front += 1
        i, j = q[front]
        # i, j = q[front]
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj # 익은 토마토의 인접칸
            if 0<=ni<N and 0<=nj<M and tomato[ni][nj]==0 and visited[ni][nj]==0:  # 인접 칸에 안익은 토마토가 들어있으면
                rear += 1  # q.appned((ni, nj))
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1

    # 익지 않은 토마토가 있으면 -1 리턴
    # 모두 있은 경우 visited 최대값 리턴
    maxV = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j]==0 and visited[i][j]==0:
                return -1
            elif maxV < visited[i][j]: # 익은 날짜 비교
                maxV = visited[i][j]
    return maxV -1

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
