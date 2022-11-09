numbers = []
for number in range(9):
    numbers.append(int(input()))

max_num = 0
max_num_idx = -1
for i in range(9):
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_num_idx = i + 1

print(max_num)
print(max_num_idx)
