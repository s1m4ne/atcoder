h,w = map(int,input().split())

x = [[0]*(w+1)] + [[0]+list(map(int,input().split())) for _ in range(h)]

for i in range(1,h+1):
    for j in range(1,w+1):
        x[i][j] += x[i][j-1]

for i in range(1,w+1):
    for j in range(1,h+1):
        x[j][i] += x[j-1][i]

q = int(input())

for _ in range(q):
    a,b,c,d = map(int,input().split())
    print(x[c][d] - x[c][b-1] - x[a-1][d] + x[a-1][b-1])