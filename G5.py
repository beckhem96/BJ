# N = int(input())
# tops = list(map(int, input().split()))
# # t = tops.pop()
# result = [0] * N
# for i in range(N-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if tops[j] > tops[i]:
#             idx = j+1
#             result[i] = idx
#             break
#         else:
#             result[i] = 0
#
# print(*result)

N = int(input())
tops = list(map(int, input().split()))
top = N - 1
idx = N - 1
t = tops.pop()
top -= 1
result = [0] * N
while tops:
    print(tops, top, idx, t, result)
    i = top
    while i > 0:
        if tops[i] > t:
            result[idx] = i + 1
            break
        else:
            result[idx] = 0
        i -= 1
    idx = len(tops) - 1
    t = tops.pop()
    top -= 1
print(*result)