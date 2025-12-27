# N:プリンタの台数
# A:各プリンタが何秒毎に印刷するか
# 二分探索でK枚目が印刷されていない秒までをng
# K枚目が印刷完了した以降の秒数をokとする

def is_ok(t,A,K):
    total = 0
    for a in A:
        total += t//a
    return total >= K

N,K = map(int, input().split())
A = list(map(int,input().split()))

ng, ok = -1, 10**9

while ok - ng > 1:
    mid = (ng + ok) // 2
    if is_ok(mid,A,K):
        ok = mid
    else:
        ng = mid
print(ok)