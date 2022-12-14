# 30748 KB / 1036 ms

# 기본적으로 어떤 규칙을 찾아보려고 했는데 숫자가 커질수록 닝겐의 머리로는 찾을 수 없을 것 같아서
# 숫자를 1부터 666이 포함된 N개의 숫자가 나올 때까지 돌려서 리스트에 넣고자 했음

N = int(input())                # N번째 숫자 입력

end_num = []                    # 666이 들어간 숫자들을 넣을 리스트
cnt = 0                         # 1부터 계속 증가시킬 숫자 (N개의 종말의 숫자가 나올 때까지..)
while len(end_num) < N:         # end_num의 길이가 N과 같아지면. 즉, N번째 숫자를 찾으면  while문을 멈춤
    if '666' in str(cnt):       # str 형태로 바꿔서 비교해줌
        end_num.append(cnt)     # 666이 들어가면 list에 넣어줌
    
    cnt += 1                    # 종말의 숫자든 아니든 cnt는 계속 증가

print(end_num[-1])              # 1부터 증가시켰기 때문에 가장 마지막 숫자가 N번째 종말의 숫자이므로 [-1]로 출력



N = int(input())               

end_num = []                  
cnt = 0                         
while len(end_num) < N:         
    if '666' in str(cnt):       
        end_num.append(cnt)     
    
    cnt += 1                  

print(end_num[-1])              