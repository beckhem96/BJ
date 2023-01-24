import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
C, N = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] + [100000] * C

for i in range(C):
    for cost, client in costs:
        if i + client < C:
            dp[i+client] = min(dp[i+client], dp[i] + cost)
            # 원래 있는 비용과 client 추가 되기 전 비용에 cost 붙은 것 중 최소를 쓴다.
        elif i + client >= C:
            dp[C] = min(dp[C], dp[i] + cost)
            # C값 보다 많은 손님을 유치할 수 있는데 비용이 더 저렴한 경우를 고려해서 이렇게 쓴다.
print(dp[C])