import sys
# import heapq
# from collections import deque
# import copy
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

start = 100
N = int(input().strip())
M = int(input())
wrong_button = list(map(int, input().split()))
min_count = abs(100 - N)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in wrong_button:
            break
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - N) + len(nums))

print(min_count)