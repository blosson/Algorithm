N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
new_scores = []
for score in scores:
    new_scores.append(score / max_score * 100)

new_scores_average = sum(new_scores) / N
print(new_scores_average)

