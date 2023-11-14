
# 걍 생 노가다인데 다른 방법을 찾아보겠음...

def solution(numbers, hand):
    answer = ''

    # 각 줄을 리스트로 만듦 (list의 index를 가지고 거리 계산을 할 것임)
    middle_list = [2, 5, 8, 0]
    left_list = [1, 4, 7, '*']
    right_list = [3, 6, 9, '#']
    
    # 왼손과 오른손의 위치
    left_idx = '*'
    right_idx = '#'
    
    # 왼쪽 라인이 나오면 아묻따 'L' 추가 후 왼손 인덱스 변경
    for i in numbers:
        if i % 3  == 1:
            answer += 'L'
            if i == 1:
                left_idx = 1
            elif i == 4:
                left_idx = 4
            else:
                left_idx = 7
        
        # 오른쪽 라인이 나오면 아묻따 'R' 추가 후 오른손 인덱스 변경
        elif i % 3 == 0 and (i // 3) >= 1:
            answer += 'R'
            if i == 3:
                right_idx = 3
            elif i == 6:
                right_idx = 6
            else:
                right_idx = 9
            
        # 2580일 때
        else:
            # 눌러야 할 키패드의 위치와 현재 왼손, 오른손과의 거리 
            left_distance = 0
            right_distance = 0
            # 왼손이 가운데 줄 키패드에 있을 때
            if left_idx in middle_list:
                left_distance = abs(middle_list.index(left_idx) - middle_list.index(i))
            # 왼손이 왼쪽 줄 키패드에 있을 때 (열간의 거리도 있으니 +1 추가해줘야 함)
            else:
                left_distance = abs(left_list.index(left_idx) - middle_list.index(i)) + 1
                
            # 오른손이 가운데 줄 키패드에 있을 때
            if right_idx in middle_list:
                right_distance = abs(middle_list.index(right_idx) - middle_list.index(i))
            # 오른손이 오른쪽 줄 키패드에 있을 때
            else:
                right_distance = abs(right_list.index(right_idx) - middle_list.index(i)) + 1
            
            # 눌러야 할 키패드가 왼손, 오른손 중 어느 하나가 더 가까운 경우
            if left_distance < right_distance:
                answer += 'L'
                left_idx = i
            
            elif left_distance > right_distance:
                answer += 'R'
                right_idx = i
                
            # 거리가 같은 경우
            else:
                if hand == 'left':
                    answer += 'L'
                    left_idx = i
                else:
                    answer += 'R'
                    right_idx = i
    return answer