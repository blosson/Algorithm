
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

spin90 = []
for j in range(N):
    plus_list = []
    for i in range(N-1, -1, -1):
        print(numbers[i][j], end = '')
    print()

for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        print(numbers[i][j], end = '')
    print()

for j in range(N-1, -1, -1):
    for i in range(N):
        print(numbers[i][j], end = '')
    print()
