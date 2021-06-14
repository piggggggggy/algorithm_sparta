# 평균은 넘겠지_하_1차원 배열

n = int(input())
for i in range(n):
    scores = list(map(int, input().split()))
    nn = scores.pop(0)
    avg = sum(scores)/nn
    avgup = [j for j in scores if j > avg]
    result = len(avgup)/nn
    print('%.3f' % round(result*100, 3)+'%')