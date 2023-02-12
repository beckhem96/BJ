import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
answer = []
queue = deque()
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1 # 진입 차수 표시
for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)
while queue:
    tmp = queue.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)
print(*answer)