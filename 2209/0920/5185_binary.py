conversion = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}    

for tc in range(1, int(input()) + 1):
    
    N, hexadecimal = input().split()
    
    ans = ''
    for n in hexadecimal:
        if n in conversion:             # 10~15 사이일 경우
            number = conversion[n]

        else:                           # 0~9일 경우
            number = int(n)


