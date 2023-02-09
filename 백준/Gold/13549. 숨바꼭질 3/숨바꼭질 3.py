import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000000)
from collections import deque

MAX = 1000001
N, K = map(int, input().split())
q = deque()
q.append(N)
check = [0] * MAX # 방문 했는지 확인
dist = [-1] * MAX # 걸린 시간?거리 기록
check[N] = 1
dist[N] = 0
while q:
    i = q.popleft()
    if 0<=i*2<MAX and not check[i*2]:
        q.appendleft(i*2) # 왜 순간이동은 맨 앞에 넣을까
        check[i*2] = 1
        dist[i*2] = dist[i]
    if 0<=i-1<MAX and not check[i-1]:
        q.append(i-1)
        check[i-1] = 1
        dist[i-1] = dist[i] + 1
    if 0<=i+1<MAX and not check[i+1]:
        q.append(i+1)
        check[i+1] = 1
        dist[i+1] = dist[i] + 1
print(dist[K])