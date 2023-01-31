import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [100001]* (k+1) # 가치의 합인 k까지의 10만(동전가치의 최댓값)을 값으로 넣어준다
# dp[숫자]에 들어있는 건 숫자를 만드는데 든 최소의 동전 수
dp[0] = 0 # 합이 0인건 0

for coin in coins:
    for i in range(coin, k+1): # 현재 동전 값에서 합까지의 수를
        dp[i] = min(dp[i], dp[i - coin] + 1)
        # 현재 경우의 수와
        # 현재 값에서 현재 동전의 값을 뺀 경우의 수에 플러스 1(현재 동전을 더 한 경우)
if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])