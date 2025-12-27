h,w,n = map(int,input().split())

z = [[0]*(w+2) for _ in range(h+2)]

for _ in range(n):
    a,b,c,d = map(int,input().split())
    z[a][b] += 1
    z[c+1][d+1] += 1
    z[a][d+1] -= 1
    z[c+1][b] -= 1

for i in range(1,h+1):
    for j in range(1,w+1):
        z[i][j] += z[i][j-1]

for i in range(1,w+1):
    for j in range(1,h+1):
        z[j][i] += z[j-1][i]

for row in z[1:h+1]:
    print(*row[1:w+1])

# 配列は1つ分だけ大きく定義する
# 長方形領域が端までの大きさのとき+1や-1を代入できなくなる
# ただし累積和での計算は範囲外で使用されないのでしなくてOK