# <IDEA>
# - 2차원 배열을 차례로 순회하면서 숫자인 곳들을 탐색
# - 숫자인 부분을 델타 탐색하면서 그 합들을 구해줌, 방문한 곳은 visited 표시
# - 모두 탐색했으면 answer 배열에 넣어줌
# - answer 배열 오름차순 정렬

# DFS 풀이
def solution(maps):                       
    dx = [-1, 0, 1, 0]                      # 델타 탐색
    dy = [0, 1, 0, -1]
    answer = []
    
    maps2 = []
    for map in maps:                        # 방문표시 편하게 하기 위해 maps2를 리스트로 바꿔줌
        maps2.append(list(map))
    
    for i in range(len(maps2)):
        for j in range(len(maps2[0])):
            if maps2[i][j] != 'X':          # 숫자가 나오면 stack에 넣어주고 탐색 준비
                stack = []
                cnt = 0
                stack.append((i, j))
                
                while stack:                # stack에서 꺼내서 탐색하기
                    now = stack.pop()
                    x, y = now[0], now[1]
                    if maps2[x][y] == 'X':  # 방문한 곳이면 continue
                        continue
                        
                    cnt += int(maps2[x][y]) # 방문한 곳이 아니면 방문처리 해주고, 숫자+해주기
                    maps2[x][y] = 'X'
                    
                    for k in range(4):      # 델타 탐색
                        tx, ty  = x + dx[k], y + dy[k]
                                            # 인덱스 범위 안에 있고 방문한 곳이 아니면 stack에 넣어줌
                        if 0 <= tx < len(maps2) and 0 <= ty < len(maps2[0]):
                            if maps2[tx][ty] != 'X':
                                stack.append((tx, ty))
                answer.append(cnt)          # stack 탐색 완료하면 결과값을 answer에 넣어줌
    
    if answer:                              # 무인도 있으면 정렬하여 return
        answer.sort()
    else:                                   # 없으면 [-1] return
        answer = [-1]
                 
    return answer