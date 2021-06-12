#
# a = [6,9,5,7,4]
#
# print(sum(a[5:]))
#
# b = [{"a":2},{"b":3},{"c":5},{"a":9}]
#
# print(len(b["a"]))

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
dict = {}
n = len(genres)
for i in range(n):
    dict[genres[i]] += plays[i]

print(dict)