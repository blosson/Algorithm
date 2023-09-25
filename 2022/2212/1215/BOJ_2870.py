# 40ms
'''
어떻게 숫자와 문자를 분리시킬건지 고민을 많이 했음.
딱히 방법이 떠오르지 않아서 조건을 세분화 한 다음, 일일이 if 문으로 쪼개주는 방법을 선택함
'''
N = int(input())                                        # 줄 갯수

alphabet = 'abcdefghijklmnopqrstuvwxyz'                 # 소문자와 숫자로만 이루어져 있으므로 체크용 알파벳 문자열
num_list = []                                           # 숫자들을 담을 리스트

for _ in range(N):                                      # 줄 만큼 반복
    words = input()                                     # 단어 입력 받기 (str임에 주의)

    cnt = 0                                             # 자기자신 앞까지 숫자가 몇 번 연속으로 있는지 체크하는 변수

    for i in range(len(words)):                         # 문자의 길이만큼 순회

        if words[i] in alphabet:                        # 만약 해당 words[i]가 숫자가 아닌 '문자'라면
            # print('yes')
            if cnt:                                     # 앞서 숫자로 계속 이어져왔으면 (cnt >= 1)
                num_list.append(int(words[i-cnt:i]))    # 해당 cnt 만큼 자기 자신 앞까지 슬라이싱 해서 num_list에 넣어줌. 
                                                        # 예를 들어, 이때 017 이런 것들은 int()를 넣어주니까 알아서 0이 떼어져서 개꿀임
                cnt = 0                                 # 문자가 등장했으니 다시 cnt = 0으로 바꿔줌

                                                            
        else:                                                   # 현재 글자가 숫자라면
            if i == len(words) - 1:                             # 숫자가 마지막으로 끝날 때 : 마지막 인덱스 번호 = 길이-1 (words 전체가 숫자일 때는 어차피 여기에 포함되므로 굳이 고민 X)
                if cnt:                                         # 자기 바로 앞에 숫자가 있었으면
                    num_list.append(int(words[i-cnt:i+1]))      # 해당 cnt만큼 자기 자신 포함 슬라이싱 해서 num_list에 넣어줌
                else:
                    num_list.append(int(words[i]))              # 앞이 숫자가 아니었으면 그냥 자기 자신만 num_list에 넣어줌

            else:                                               # 현재 숫자가 words의 마지막 글자가 아닐 때
                cnt += 1                                        # 다음 것 확인할 수 있도록 cnt만 +1

num_list = sorted(num_list)                                     # 비내림차순은 그냥 오름차순이랑 똑같음 말장난 ㄴㄴ ㅡㅡ
# print(num_list)

for num in num_list:                                            # 하나씩 살포시 출력해주면 완성!
    print(num)
