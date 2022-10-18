test = input()

#1 슬라이싱 (내 풀이)
ans = False
if test == test[::-1]:
    ans = True

print(ans)

#2 리스트로 변환 (교재 참고)
test_list = []
for i in test:
    test_list.append(i)

ans = True
while len(test_list) > 1:                       # pop 아이디어
    if test_list.pop(0) != test_list.pop():
        ans = False
        break

print(ans)

#3 deque - 공부해볼 필요 O
#4 C구현은 또 뭔지..



    
