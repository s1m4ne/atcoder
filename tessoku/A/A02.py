# input()は標準入力・常に文字列として受け取る
# split()はスペースまたはカンマ等で分割しリストを作るもの
# map()は左に指定した関数を右側に指定したイテラブルの各要素に適用する

# 

n,x = map(int,input().split())
a = list(map(int,input().split()))

ans = "No"

for num in a:
    if num == x:
        ans = "Yes"
        
print(ans)
