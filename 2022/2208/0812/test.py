# T : target / P : pattern

def pre_process(P):
    lps = [0] * len(P)

    # lps를 만들기 위한 prefix에 대한 idx,
    j = 0
    
    """
    i : pattern에서 지나가고 있는 id
    j : 지나가고 있는 idx와 pattern의 앞부분과 같은 부분에 대한 idx
    """

    # 처음부터 끝까지 순회를 돌면서
    for i in range(1, len(P)):
        # i 와 j가 같으면 lps의 i 자리에 j+1을 넣어줍니다. (prefix idx 위치에 있는 char와 같으면 lps에 숫자 추가)
        if P[i] == P[j]:
            lps[i] = j + 1
            j += 1
        # 다르다면, j를 초기화 해주어 pattern의 가장 처음부터 인식하도록 합니다.
        # 그 자리에서 기존의 j자리(비교를 하고 있던 자리)가 아닌 pattern 처음으로 돌아가 비교를 해줍니다.
        else:
            j = 0
            if P[i] == P[j]:
                lps[i] = j + 1
                j += 1

    return lps

T = 'abcdabeeababcdabcef'
P = 'eaba'

lps = pre_process(P)
print(lps)