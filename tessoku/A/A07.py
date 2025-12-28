d = int(input())
n = int(input())

diff = [0] * (d + 2)

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

for i in range(1, d + 2):
    diff[i] += diff[i - 1]

for i in range(1, d + 1):
    print(diff[i])
