# Homework 3
# P166
# Time limit = 3s


test = int(input())
for _ in range(test):
    n = int(input())
    w = [int(i) for i in input().split()]
    # code here
    ww = []
    for i in range(n):
        ww.append((w[i], i))
    ww = sorted(ww)
    box_order = []
    for i in range(n):
        box_order.append(ww[i][1]+1)
    # output
    print(' '.join(map(str, box_order)))