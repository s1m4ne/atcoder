n, x = map(int,input().split())
a = [0] + list(map(int,input().split()))

l, r = 1, n
while l <= r:
    m = (l + r) // 2
    if a[m] == x:
        print(m)
        break
    elif a[m] < x:
        l = m + 1
    else:
        r = m - 1


# 標準ライブラリを用いた回答

# import bisect

# n, x = map(int, input().split())
# a = [0] + list(map(int, input().split()))

# idx = bisect.bisect_left(a, x)    # 今回は値の重複が無いのでbisect_left()でもbisect_right()でもbisect()でも良い
# print(idx)