import sys
input = sys.stdin.readline
def go_eat(i, j):
    visited = [[0]*N for _ in range(N)] # 걸린 시간 확인하는 배열
    qe = [(i, j)]
    visited[i][j] = 1
    fishes = []
    while qe:
        si, sj = qe.pop(0)
        for di, dj in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            ni, nj = si+di, sj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                if arr[ni][nj] == 0 or arr[ni][nj] == shark:
                    visited[ni][nj] = visited[si][sj] + 1
                    qe.append((ni, nj))
                elif 0<arr[ni][nj]<shark:
                    visited[ni][nj] = visited[si][sj] + 1
                    qe.append((ni, nj))
                    fishes.append((ni, nj, visited[ni][nj]))
    fishes.sort(key=lambda x : (x[2], x[0], x[1]))
    if len(fishes) == 0:
        return -1, -1, -1
    else:
        return fishes[0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = 2 # 상어 크기
result, eaten = 0, 0 # 결과(시간), 먹은 물고기 수

q = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            q.append((i, j))# 현재 상어 위치 넣기

while q:
    i, j = q.pop(0)
    arr[i][j] = 0
    si, sj, cnt = go_eat(i, j)
    if cnt == -1:
        break
    else:
        q.append((si, sj)) # 다음 상어 ㄱㄱ
        result += cnt-1 # 걸린 시간
        eaten += 1 # 먹은 물고기 세고
        if eaten == shark: # 먹은 물고기 수가 상어 크기면
            shark += 1 # 상어 1단계 진화
            eaten = 0

print(result)
