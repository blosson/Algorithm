TC = int(input())
for _ in range(TC):
    times, S = input().split()

    times = int(times)

    # print(times)
    # print(S)

    for i in S:
        for time in range(times):
            print(i, end="")
    print()


