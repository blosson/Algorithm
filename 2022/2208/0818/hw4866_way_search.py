# 아직 못 풀어서 일단 다른 팀원 걸로 제출합니다 ㅠㅠ


for tc in range(10):# input 받는 구간
    
    t, E = map(int, input().split())
    edge_list = [[] for _ in range(100)]
    edge_input = list(map(int, input().split()))
    
		# 리스트 만들어주는 구간, edgelist를 input에 맞춰 설정
    for i in range(E): 
        start = edge_input[i * 2] # start node
        end = edge_input[i * 2 + 1] # end node
        edge_list[start].append(end) # [[]]
    '''
    [0 == edge_input[i*2] == start, 1 == edge_input[i*2+1] == end, 0 == start, 2 == end, 1, 4, 1, 3, 4, 8, 4, 3, 2, 9, 2, 5, 5, 6, 5, 7, 7, 99, 7, 9, 9, 8, 9, 10, 6, 10, 3, 7]'''
    # -> [[1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10], [], [], [], [],....]

    visited = [False]*100 # 방문여부 체크를 위한 visited
    stack =[0] # stack 

    while stack: # stack == True # 스택이 빌 때까지 pop, append 반복
        current = stack.pop() # current란 변수를 현재 노드로 설정해주고
        
        if not visited[current]: # 방문하지 않았다면
            visited[current] = True # 업데이트 ex: [False, False, False, False, False] -> [True, False, False, False, False]
            
            for v in edge_list[current]: # edge_list[현재값] ex: edge_list[0] == [1,2]
                if not visited[v]: # 방문 표시 없다면
                    stack.append(v) # 스택에 쌓아줌 ->  과정을 반복
                    
    if visited[99] == 1:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")