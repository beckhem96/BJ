N = int(input())
books = []
nums = []
result = []
for _ in range(N):
    book = input()
    if book in books:
        nums[books.index(book)] += 1
    else:
        books.append(book)
        nums.append(1)

for i in range(len(nums)):
    if max(nums) == nums[i]:
        result.append(books[i])
result.sort()
print(result[0])