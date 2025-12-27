d = int(input())
n = int(input())
s = [0] * (d+2)

for i in range(n):
    l,r = map(int,input().split())
    s[l] += 1
    s[r+1] -= 1
    
for i in range(1,d+2):
    s[i] += s[i-1]

for i in range(1,d+1):
    print(s[i])