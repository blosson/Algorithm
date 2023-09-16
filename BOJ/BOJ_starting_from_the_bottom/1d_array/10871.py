n, x = map(int, input().split())
A = list(map(int, input().split()))

smalls = []
for a in A:
    if a < x:
        smalls.append(a)

print(*smalls)