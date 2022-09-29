# 도저히 못 풀겠어서 동준님 걸로 가져와서 조금이나마 이해하고 제출합니다.
# 그런데 갈수록 알고리즘이 너무 어려운데 어떡하죠...

check = "123456789ABCEF"
st_to_two = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
pat = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}


def trans16to2(code1):
    two = ''
    for q in code1:
        for i in q:
            two += st_to_two.get(i)
    return two



for tc in range(int(input())):
    garo, sero = map(int, input().strip().split())
    secret = [input().strip()[::-1].lstrip("0") for _ in range(garo)]
    codes = []

    for s in secret:
        if not s:
            continue
        i = 0
        while 1:
            if i >= len(s)-15:
                break

            if s[i] in check:
                if s[i:i+15][::-1] not in codes:
                    codes.append(s[i:i+15][::-1])
                    i += 15
                else:
                    i += 15
            else:
                i += 1
    # print(codes)                    
    two_codes = []
    for c in codes:
        two_codes.append(trans16to2(c))               
    # print(two_codes)

    ans = []
    for two in two_codes:
        for m in range(len(two)-7):
            res = ''
            while m<len(two):
                if m >= len(two)-6:
                    break
                if two[m:m+7] in pat:
                    res += str(pat.get(two[m:m+7]))
                    m += 7
                else:
                    m += 1
            if len(res) == 8:
                if list(map(int, res)) not in ans:
                    ans.append(list(map(int, res)))
            elif len(res) == 7:
                if list(map(int, res))+[0] not in ans:
                    ans.append(list(map(int, res))+[0])
                
    # print(ans)

    real = []
    for ans1 in ans:
        if len(ans1) < 8:
            continue
        zak = 0
        hol = 0   
        for idx, a in enumerate(ans1):
            if idx == 7:
                zak += a
            elif idx%2:
                hol += a
            else:
                zak += a*3
        if (zak + hol)%10:
            real.append(0)
        else:
            real.append(sum(ans1))
    print(f"#{tc+1} {sum(real)}")