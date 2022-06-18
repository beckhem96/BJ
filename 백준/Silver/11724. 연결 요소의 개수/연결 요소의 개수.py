import sys
sys.setrecursionlimit(5000)

def dfs(v):
    # 방문 표시
    visited[v] = 1

    # 해당 노드의 인접 노드에 접근
    for j in adj[v]:
        if not visited[j]: # 인접 노드에 방문 한 적없으면
            visited[j] = 1
            dfs(j) # 재귀로 다 접근

N, M = map(int, input().split())

# 인접행렬
adj = [[] for _ in range(N+1)]
# 연결 요소 개수
cnt = 0
# 노드 방문 표시
visited = [0] * (N + 1)

# 인접 표현 행렬에 저장
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N+1):
    # 노드 만큼 반복
    if not visited[i]: # 노드에 방문한 적 없으면
        dfs(i) # 함수 실행
        # 함수가 끝나면 들어간 노드의 인접 노드는 다 방문
        cnt += 1 # 연결 요소 개수 세기

print(cnt)