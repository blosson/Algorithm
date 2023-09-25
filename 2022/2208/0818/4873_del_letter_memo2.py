# 나연님 방법인데 이게 훨씬 깔끔하고 예쁘게 stack을 구현한 것 같다.

def lenlen(a):
    cnt = 0
    for i in a:
        cnt += 1
    return cnt

word = input()
stack = []
for i in word:
    if not stack or stack[-1] != i:
        stack.append(i)
    else:
        stack.pop()

print(lenlen(stack))

