arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subsets = [[]]

for num in arr:
  size = len(subsets)
  for y in range(size):
    subsets.append(subsets[y]+[num])

ans_list = []
for i in subsets:
    if sum(i) == 10:
        ans_list.append(i)

print(*ans_list)