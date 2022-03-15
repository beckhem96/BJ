def bfs(i, j, N):
    # visited 생성 (이미 생성)
    q = [] # 큐 생성
    q.append((i,j)) # 시작점 인큐
    v[i][j] = 1 # 단지에 포함
    h = 0  # 단지에 속한 집의 수
    while q:
        i, j = q.pop(0) # 디큐
        h += 1 # visit()
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj] = 1 # 단지에 속한 집으로 인큐됨
    return h
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# arr = [input() for _ in range(N)] 문자열 사용시
cnt = 0     # 단지 수
num = []    # 단지에 속한 집의 수
v = [[0]*N for _ in range(N)] # 단지에 속했는지 표시
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j]==0: # 아직 단지에 속하지 않은 집을 만나면
            cnt += 1 # 새로운 단지, 단지 수 증가
            r = bfs(i, j, N) # 단지에 속한 집의 수
            num.append(r)
num.sort()
print(cnt) # 단지 수 출력
for x in num: # 단지에 속한 집의 수 출력
    print(x)