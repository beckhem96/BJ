import sys
import heapq

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N = int(input())
result = 0
p_nums = []
m_nums = []
is_zero = False
for _ in range(N):
    tmp = int(input())
    if tmp > 1:
        p_nums.append(tmp)
    elif tmp == 1:
        result += 1
    elif tmp == 0:
        is_zero = not is_zero
    else:
        m_nums.append(tmp)
p_nums.sort(reverse=True)
m_nums.sort()

if len(p_nums) % 2 == 0:
    for i in range(0, len(p_nums), 2):
        result += p_nums[i] * p_nums[i+1]
else:
    for i in range(0, len(p_nums)-1, 2):
        result += p_nums[i] * p_nums[i + 1]
    result += p_nums[-1]

if len(m_nums) % 2 == 0:
    for i in range(0, len(m_nums), 2):
        result += m_nums[i] * m_nums[i+1]
else:
    for i in range(0, len(m_nums)-1, 2):
        result += m_nums[i] * m_nums[i + 1]
    if not is_zero:
        result += m_nums[-1]
print(result)