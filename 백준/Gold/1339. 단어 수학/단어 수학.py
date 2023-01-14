import sys
# import heapq

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N = int(input())
alpha = []
alpha_dict = {}
num_list = []
for _ in range(N):
    alpha.append(input().rstrip())
for i in range(N):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_dict:
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i]) - j - 1)
        else:
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i]) - j - 1)

for val in alpha_dict.values():
    num_list.append(val)
num_list.sort(reverse=True)
multi = 9
for i in range(len(num_list)):
    num_list[i] = num_list[i] * multi
    multi -= 1
print(sum(num_list))