def son(pattern, target):
    
    pattern_len  = len(pattern)
    target_len = len(target)

    i = j = 0 # i : target index / j : pattern index

    while i < target_len and j < pattern_len:
        if pattern[j] != target[i]:
            i = i - j
            j = - 1
        i += 1
        j += 1

    if j == pattern_len: # index j와 pattern의 길이가 같아지면 (= 패턴이 존재하면)
        return 1
    else:
        return 0
        
for tc in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()

    print(f'#{tc} {son(str1, str2)}')
