def binary_search(start_node):
    pass

def inorder(n):                 # 중위순회
    if n:
        if (n*2) <= N:
            inorder(n*2)
        order_list.append(n)
        if (n*2 + 1) <= N:
            inorder(n*2 + 1)

# def inorder(node):
#     global N                
#     if node:
#         if (node * 2) <= N:
#             inorder(node_list[node * 2])
#         node_list[node] = 1
#             inorder(ch2[n])

N = int(input())
# temp = N
order_list = []
node_list = [0] * (N + 1)

# cnt = 0
# while True:
#     if N / 2 >= 1:
#         N = N / 2
#         cnt += 1
#     else:
#         break
# N = temp
# start_node = 2 ** (cnt)
inorder(1)

k = 1
for i in order_list:
    node_list[i] = k
    k += 1

print(node_list)
    