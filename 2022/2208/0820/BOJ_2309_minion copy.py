m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
m6 = int(input())
m7 = int(input())
m8 = int(input())
m9 = int(input())

height_list = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
height_sum = sum(height_list)
height_diff = height_sum - 100

print(height_diff)
for i in range(9):
    for j in range(9):
        if i != j:
            if height_list[i] + height_list[j] == height_diff:
                del1 = height_list[i]
                del2 = height_list[j]
                height_list.remove(del1)
                height_list.remove(del2)
                break
                break

print(height_list)
                
