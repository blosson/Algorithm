pieces = list(map(int, input().split()))
right_pieces = [1, 1, 2, 2, 2, 8]


ans = [0] * 6
for i in range(6):
    if pieces[i] != right_pieces[i]:
        ans[i] = right_pieces[i] - pieces[i]

print(*ans)