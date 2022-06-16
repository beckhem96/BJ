N = int(input())
brackets = []
for _ in range(N):
    brackets.append(list(map(str, input())))

for _ in range(len(brackets)):
    bracket = brackets.pop(0)
    VPS = []
    while bracket:
        br = bracket.pop(0)
        if br == '(':
            VPS.append(br)
        else:
            if len(VPS) and VPS[-1] == '(':
                del VPS[-1]
            else:
                VPS.append(br)
    if len(VPS):
        print('NO')
    else:
        print('YES')