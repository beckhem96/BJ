import sys
import heapq

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
jews = []
bags = []

result = 0
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jews, [m, v])
for _ in range(K):
    bags.append(int(input()))

bags.sort()
tmp_jew = []
for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jews)[1])
    if tmp_jew:
        result -= heapq.heappop(tmp_jew)
    elif not jews:
        break
print(result)