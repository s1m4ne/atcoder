n = int(input())
a = [0] + list(map(int, input().split())) + [0]

p = [0]*(n+2)
for i in range(1,n):
    p[i] = max(p[i-1],a[i])

q = [0]*(n+2)
for i in range(n,1,-1):
    q[i] = max(a[i],q[i+1])
    
d = int(input())

for i in range(d):
    l,r = map(int,input().split())
    print(max(p[l-1],q[r+1]))