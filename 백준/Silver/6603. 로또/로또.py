# def f(n, k, m):    # 순열 p[n]을 채우는 함수. k 고를 개수, m 주어진 숫자 개수
#     if n==k:
#         if sorted(p) not in test:
#             print(*sorted(p), sep=' ')
#         test.append(sorted(p))
#     else:
#         for i in range(m): # used에서 사용하지 않은 숫자 검색
#             if used[i] == 0:    # 앞에서 사용하지 않은 숫자인 경우
#                 used[i] = 1     # 사용함으로 표시
#                 p[n] = arr[i]     # p[n] 결정
#                 f(n+1, k, m)
#                 used[i] = 0     # a[i]를 다른 위치에서 사용할 수 있도록 함
#     return
# 위 코드로 풀면 시간초과가 난다.

def dfs(depth, idx):
    if depth == 6:
        print(*out)
        return

    for i in range(idx, K):
        out.append(S[i])
        dfs(depth + 1, i + 1)
        out.pop()

while 1:
    input_arr = []
    input_arr = list(map(int, input().split()))
    if input_arr[0] == 0:
        break
    test = []
    K = input_arr[0]
    S = input_arr[1:]
    out = []
    dfs(0, 0)
    print()