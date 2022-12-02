word = input().upper()
word_set = set(map(str, word))      # 중복을 줄이기 위해 set을 만들어줌

# print(word_set)

max_cnt = 0
ans = '?'
for s in word_set:
    s_cnt = word.count(s)
    if s_cnt > max_cnt:
        max_cnt = s_cnt
        ans = s

for s in word_set:
    if word.count(s) == max_cnt and ans != s:
        ans = '?'

print(ans)


# 딕셔너리로도 풀 수 있다!!!

# input_str = input().upper()
# letter_counts = {}
# for letter in input_str:
#     letter_counts[letter] = letter_counts.get(letter, 0) + 1

# max_a = 0
# for key, value in letter_counts.items():
#     if value > max_a:
#         max_key = key
#         max_a = value

#     elif value == max_a:
#         max_key = '?'

# print(max_key)



