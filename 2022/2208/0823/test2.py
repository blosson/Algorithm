arr = [1, 2, 3]
subsets = [[]] # 부분집합을 담을 녀석

def d_sup():
    for sub in subsets:
        if sum(sub) == 10:
            print(sub)


# 부분집합 구하는 for 문 (복습해서 과정 이해해보자)
for num in arr:
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [num])
        print(subsets)

print()
d_sup()
