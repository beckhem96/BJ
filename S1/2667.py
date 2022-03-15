#<그림 1>과 같이 정사각형 모양의 지도가 있다.
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
start_i, start_j = 0, 0
danji = 0 # 단지 수
num = [] # 단지 내의 집 수

q = [] # 큐생성

v = [[0]*N for _ in range(N)] # 방문했는지

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] == 0: # 단지에 속하지 않은 집을 만난다면
            danji += 1
            q.append((i,j)) # 시작점 인큐
            v[i][j] = 1
            house = 0
            while q:
                i, j = q.pop(0) # 디큐
                house += 1
                for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                    ni, nj = i + di, j + dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1 and v[ni][nj] == 0:
                        q.append((ni, nj))
                        v[ni][nj] = 1
            num.append(house)
num.sort()
print(danji)
for result in num:
    print(result)


