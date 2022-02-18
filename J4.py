together = []
separated = []
groups = []
for _ in range(int(input())):
    together.append(input().split())
for _ in range(int(input())):
    separated.append(input().split())
for _ in range(int(input())):
    groups.append(input().split())
partners = {}                               # dict storing the people in the same group as [i] in partners[i]
for i in groups:                            # decreases the time complexity from O(n^3) to O(n^2) compared to traversing
    for j in i:                             # [groups] for every rule
        partners[j] = i
v = 0
for i in together:
    if i[1] not in partners[i[0]]:
        v += 1
for i in separated:
    if i[1] in partners[i[0]]:
        v += 1
print(v)
