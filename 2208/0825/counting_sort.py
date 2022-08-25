numbers = [5, 4, 1, 1, 3, 2, 5, 2, 4, 4, 3, 0]

max_num = 0
len_numbers = 0
for num in numbers:
    len_numbers += 1
    if num > max_num:
        max_num = num

sorted_numbers = ['-'] * len_numbers
count_list = [0] * (max_num + 1)

for i in range(len_numbers):
    count_list[numbers[i]] += 1

for i in range(1, max_num + 1):
    count_list[i] += count_list[i-1]

for i in range(len_numbers):
    count_list[numbers[i]] -= 1
    sorted_numbers[count_list[numbers[i]]] = numbers[i]

print(sorted_numbers)
    

