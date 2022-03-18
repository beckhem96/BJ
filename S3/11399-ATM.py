# def sunyul(i, n): # 순열로 푸는 건줄 알았다...
#     global minV
#     if i == n:
#         s = 0
#         for i in range(N):
#             s += sum(P[:i+1])
#         if s < minV:
#             minV = s
#             print(P)
#     else:
#         for j in range(i, N):
#             P[i], P[j] = P[j], P[i]
#             sunyul(i+1, N)
#             P[i], P[j] = P[j], P[i]
#     return minV
#
#
# N = int(input())
# P = list(map(int, input().split()))
# i = 0
# minV = 9999
# sunyul(i, N)
# print(sunyul(i, N))

N = int(input())
P = list(map(int, input().split()))
P.sort() # 정렬하고 앞에서 부터 하나씩 더하면 작은 수 부터 더해져서 가장 작은 합이 될 수 있다.
result = []
for i in range(N):
    result.append(sum(P[:i+1]))
print(sum(result))

