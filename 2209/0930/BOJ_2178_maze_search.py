'''
1. 경로를 탐색하는 dfs 함수를 만든다. (최소가 나오니까 bfs가 나으려나..?) - 구체적인 방법은?(visited?)
2. min_cnt, cnt 변수를 만들어서 최솟값을 비교하는 코드를 함수 중간에 넣어서 백트래킹
'''

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

    