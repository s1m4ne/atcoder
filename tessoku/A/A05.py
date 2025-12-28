n, k = map(int, input().split())
c = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if 1 <= k - i + j <= n:
            c += 1
print(c)
