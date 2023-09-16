S = input()

alphabet = []
for i in set(range(97, 123)):       # This idea was sexy..
    alphabet.append(chr(i))
    
# print(alphabet)

ans = []
for i in alphabet:
    ans.append(S.find(i))           # find 메서드 사용

print(*ans)





