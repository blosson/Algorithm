n, m = map(int, input().split())

n_list = [input() for _ in range(n)]
m_list = [input() for _ in range(m)]

cnt = 0
for m_word in m_list:
    if m_word in n_list:
        cnt += 1

# for n_word in n_list:
#     for m_word in m_list:
#         if n_word == m_word:
#             cnt += 1

print(cnt)


