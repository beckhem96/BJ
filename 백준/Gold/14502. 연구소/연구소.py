def spread_virus():
    visited = [[0]*(M) for _ in range(N)]

    while virus:
        i, j = virus.pop()
        visited[i][j] = 1

        for di, dj in [[1,0],[0,1],[-1,0], [0,-1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and not arr[ni][nj] and not visited[ni][nj]:
                arr[ni][nj] = 2
                virus.append((ni, nj))

def remove_virus():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                arr[i][j] = 0

def get_start_virus():
    for i, j in start_virus:
        arr[i][j] = 2


def nCr(n, r, s): # n개에서 r개를 고르는 조합, s 고를 수 있는 구간의 시작 인덱스
    global result, virus
    if r == 0:
        cnt = 0
        for i, j in comb:
            arr[i][j] = 1 # 조합의 경우의 수를 1로 채움

        spread_virus() # 바이러스 퍼지고
        virus = start_virus.copy()

        for i in range(N):
            for j in range(M):
                if not arr[i][j]:
                    cnt += 1 # 안전지대를 셈

        if result < cnt:# 최대인가
            result = cnt


        remove_virus() # 퍼진 바이러스 제거
        get_start_virus() # 초기 바이러스 표시

        for i, j in comb:
            arr[i][j] = 0 # 조합의 경우의 수를 0으로 돌려놓음
    else:
        for i in range(s, n-r+1):
            comb[r-1] = empty[i]
            nCr(n, r-1, i+1)

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
empty = []
virus = []
start_virus = []
result = 0

for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            empty.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
            start_virus.append((i, j))

n = len(empty)
r = 3
comb = [0] * 3

nCr(n, r, 0)
print(result)