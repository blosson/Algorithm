char = input()

odd_list = []
for i in range(len(char)): # 문자열 각 index 순회
    if char.count(char[i]) % 2 == 1: # 해당문자가 홀수개
        odd_list.append(char[i]) # 홀수 리스트에 추가
       

ans = ''.join(sorted(list(set(odd_list)))) # set으로 중복값 없앤 뒤 오름차순 정렬(리스트->문자열)
print(ans)
    


# xxyy, aaaa와 같이 전부 짝수로만 이루어져 'Good'을 출력할 수 있게 해주는 코드는 어떻게 짤 수 있을까..    
