import sys
import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
visited = [0] * (V+1)
visited[K] = 1

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        w, u = heapq.heappop(q)
        if dist[u] < w:
            continue
        for next in graph[u]:
            cost = w + next[1] # 현재 노드 가중치랑 연결된 노드의 가중치를 더해서
            if dist[next[0]] > cost: # 다음 노드의 거리가 현재 노드를 통한 거리보다 크면
                dist[next[0]] = cost # 최단 거리로 갱신
                heapq.heappush(q, (cost, next[0])) # 갱신된 거리와 다음 노드를 q에 넣어줌

dijkstra(K)

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])