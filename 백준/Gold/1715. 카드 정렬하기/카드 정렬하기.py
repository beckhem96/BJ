import sys
import heapq

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

cards = []
result = 0

N = int(input())
for i in range(N):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(result)
else:
    for i in range(N-1): # 2개씩 꺼내기 때문에 N-1
        previous = heapq.heappop(cards)
        current = heapq.heappop(cards)

        result += previous + current
        heapq.heappush(cards, previous + current)
    print(result)