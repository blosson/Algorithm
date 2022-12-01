# 메모리 30840KB / 시간 232ms

numbers = []
for i in range(1, 10001):
    numbers.append(i)

for num in range(1, 10001):

    copied_num = num
    while copied_num / 10 != 0:
        num += copied_num % 10
        copied_num = copied_num // 10

    if num in numbers:
        numbers.remove(num)

for number in numbers:
    print(number)




            