N,M,K = map(int,input("세 개의 값 입력 ").split())
numbers = list(map(int,input("배열 입력").split()))

sorted = sorted(numbers,reverse=True)
result=[]

count=0
for i in range(M):
    if count==K:
        result.append(sorted[1])
        count=0
    else:
        result.append(sorted[0])
        count+=1
    

print(sum(result))