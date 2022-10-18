num_1 = input()
num_2 = input()

line_1 = 0
line_2 = 0
line_3 = 0
for i in range(2, -1, -1):              # 아래거
    for j in range(2, -1, -1):          # 위에거 (계속 바뀌어야 하므로)

        if i == 2:
            if j == 2:
                line_1 += int(num_2[i]) * int(num_1[j])
            elif j == 1:
                line_1 += int(num_2[i]) * int(num_1[j]) * 10
            else:
                line_1 += int(num_2[i]) * int(num_1[j]) * 100
        elif i == 1:
            if j == 2:
                line_2 += int(num_2[i]) * int(num_1[j])
            elif j == 1:
                line_2 += int(num_2[i]) * int(num_1[j]) * 10
            else:
                line_2 += int(num_2[i]) * int(num_1[j]) * 100

        else:
            if j == 2:
                line_3 += int(num_2[i]) * int(num_1[j])
            elif j == 1:
                line_3 += int(num_2[i]) * int(num_1[j]) * 10
            else:
                line_3 += int(num_2[i]) * int(num_1[j]) * 100

ans = (line_1 + line_2 * 10 + line_3 * 100)
print(line_1)
print(line_2)
print(line_3)
print(ans)

            