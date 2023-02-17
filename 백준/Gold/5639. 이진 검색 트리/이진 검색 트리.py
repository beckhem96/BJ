import sys
# import copy
# from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

nums = []
while 1:
        try:
                nums.append(int(input()))
        except:
                break

def postorder(s, e):
        if s > e:
                return
        mid = e + 1

        for i in range(s+1, e+1):
                if nums[s] < nums[i]:
                        mid = i
                        break
        postorder(s+1, mid-1) # 왼쪽 노드
        postorder(mid, e) # 오른쪽 노드
        print(nums[s])

postorder(0, len(nums)-1)
