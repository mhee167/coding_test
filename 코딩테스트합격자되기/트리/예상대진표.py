#내 풀이 
def solution(n,a,b):
    answer = 0
    aa=0
    count=n
    while count>1:
        count //= 2
        aa+=1
        
    for i in range(aa):
        if a!=b+1 or b!=a+1:
            a //= 2
            b //= 2
            answer+=1
    return answer


#정답
def solution(n,a,b):
    answer = 0
    while a != b:
            a= (a+1) // 2
            b= (b+1) // 2
            answer+=1
    return answer