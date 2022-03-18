sugar = int(input())
five = 5
three = 3
sugar_five = sugar // five
sugar_three = sugar // three

sugar_packs = []
for i in range(sugar_five+1):
    for j in range(sugar_three+1):
        result = sugar - (five*i) - (three*j)
        if result == 0:
            sugar_packs.append(i+j)
if len(sugar_packs) == 0:
    print(-1)
else:
    print(min(sugar_packs))