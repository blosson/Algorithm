# 중복된 문자를 제외하고 사전식 순서로 나열하라.

# set, sorted 활용
example = input()

example = sorted(list(set(list(example))))
ans = ''
for i in example:
    ans += i

print(ans)


# stack, sort 활용
example = input()

stack = []
for i in example:
    if i not in stack:
        stack.append(i)
stack.sort()
print(*stack, sep='')
