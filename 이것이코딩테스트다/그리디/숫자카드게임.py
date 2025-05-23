
n,m = map(int, input().split())
cards = []
for i in range(n):
    cards.append(list(map(int, input().split()))) 

result=[]
for i in range(n):
    result.append(min(cards[i]))

print(max(result))


#입력과 동시에 판별
for i in range(n):
    row = list(map(int, input().split()))
    result.append(min(row))
print(max(result))
