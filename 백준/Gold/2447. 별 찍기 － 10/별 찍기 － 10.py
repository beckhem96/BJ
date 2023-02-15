import sys
# from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

N = int(input())

def f(N):
    if N == 1:
        return ['*']
    stars = f(N//3)
    result = []
    for star in stars:
        result.append(star*3)
    for star in stars:
        result.append(star + ' '*(N//3) + star)
    for star in stars:
        result.append(star*3)
    return result

for r in f(N):
    print(r)