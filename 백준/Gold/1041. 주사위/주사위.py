import sys
# import heapq

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N = int(input())
nums = list(map(int, input().split(' ')))
if N == 1:
    nums.sort()
    print(sum(nums[0:5]))
else:
    min_nums = []
    # 마주보니까 이렇게 해야됨
    min_nums.append(min(nums[0], nums[5]))
    min_nums.append(min(nums[1], nums[4]))
    min_nums.append(min(nums[2], nums[3]))
    min_nums.sort()
    total_dension = N ** 2 * 5 #총 단면 수
    one_dension_num = 4*(N-2)*(N-1) + (N-2)**2 # 단면 하나만 노출되는 수
    two_dension_num = 4*(N-2) + 4*(N-1)
    triple = 4 * sum(min_nums[:3]) # 단면 세개 노출되는 수는 4개
    single = one_dension_num * min_nums[0]
    double = two_dension_num * sum(min_nums[:2])
    result = triple + double + single
    print(result)