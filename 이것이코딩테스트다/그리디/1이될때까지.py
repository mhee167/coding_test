n,m = map(int, input().split())

count=0
while n!=1:
    if n%m==0:
        n = n//m
        count+=1
    else:
        n=n-1
        count+=1

