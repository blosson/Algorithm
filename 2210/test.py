num_list = [1, 2, 3, 4, 5]
visited = [0] * len(num_list)
result = []

def perm(cnt, depth):
    
    if cnt == depth:
        print(result)
        return

    for i in range(len(num_list)):
        if visited[i] == 0:
            visited[i] == 1
            result.append(num_list[i])
            perm(cnt+1, depth)
            result.pop()
            visited[i] == 0

perm(0, 2) 
