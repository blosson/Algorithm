n = int(input())
arr = list([] for _ in range(n))

for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            arr[i].append(1)
            print(arr[i][j], end = ' ')
        else:
            arr[i].append(arr[i-1][j-1] + arr[i-1][j])
            print(arr[i][j], end = ' ')
    print()



