sentence = input().strip()

cnt = 0
for s in sentence:
    if s == " ":
        cnt += 1

ans = cnt + 1

if sentence == "":
    ans = 0 

print(ans)
