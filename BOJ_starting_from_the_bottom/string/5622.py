# 각 dict의 key 값들을 tuple로 묶는게 나을까 list로 묶는 게 나을까.
# => 튜플이 더 빠르다고 한다. 리스트의 경우 값이 바뀔 수 있기 때문에 여분의 storage가 필요하다고..

dial_dict = {'(A, B, C)': 3, '(D, E, F)': 4, '(G, H, I)': 5, '(J, K, L)': 6, '(M, N, O)': 7, '(P, Q, R, S)': 8, '(T, U, V)': 9, '(W, X, Y, Z)': 10}
word = input()

cnt = 0
for s in word:
    for dial_key in dial_dict:
        if s in dial_key:
            cnt += dial_dict.get(dial_key)

print(cnt)

# for dict in dial_dict:
#     if 'A' in dict:
#         print('YES')
#     else:
#         print('NO')



# print(dial_dict.get('[A, B, C]'))
# print(dial_dict)

