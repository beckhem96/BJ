import sys
# import heapq
from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
N, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1 # 이건 본인들 1, 2, 5같이 주어진 동전이 하나일 때 사용하기 위함
for i in numbers:
    for j in range(i, K+1):
        if j - i >= 0:
            dp[j] += dp[j-i] # j - i에 +i 했을 때 j 가 나오는 경우의 수를 더 해주는 것
print(dp[K])                # 예를 들어 i가 5, j가 7, j-i가 2이면 2를 만드는 경우의 수(2, 1+1)에
                            # +i(5)를 한 경우의 수를 추가해주는 것