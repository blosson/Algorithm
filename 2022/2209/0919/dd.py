password = ['1011000', '1001100', '1100100', '1011110', '1100010',
 '1000110', '1111010', '1101110', '1110110', '1101000'] # 암호코드 역순으로 작성 (뒤에서부터 읽어올거라 헷갈림 방지 위해)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())                    # 세로, 가로 입력받기

    ans = -1                                            
    for n in range(N):  
        code = input()                                  # 입력값 받기
        if int(code) != 0 and ans == -1:                # 0으로 이루어져 있는 줄 버리고, 이미 답 나왔으면 굳이 반복 X
            code = str(int(code[::-1]))                 # code를 역순으로 바꿔서 뒤에 있는 0을 제거함 (str -> int -> str 과정)

            numbers = []                                # 십진수로 변환된 숫자들을 넣어줄 리스트 
            for i in range(8):                          # 8자리 비밀번호이므로 8만큼 반복
                numbers.insert(0, password.index(code[7*i : 7*i+7]))    # 역순으로 저장된 암호코드 (총 56길이)
                                                        # 역순으로 암호코드를 끊어왔기 떄문에 항상 0번 index에 해당 숫자를 넣어줌
            check = (numbers[0] + numbers[2] + numbers[4] + numbers[6])*3 + numbers[1] + numbers[3] + numbers[5] + numbers[7] # 검증코드 확인용 변수

            if check % 10 == 0:                         # 올바른 암호
                ans = sum(numbers)
            else:                                       # 잘못된 암호
                ans = 0

    print(f"#{tc} {ans}")