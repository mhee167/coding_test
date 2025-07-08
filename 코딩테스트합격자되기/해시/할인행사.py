#틀림
# 일단 result 의미를 잘못 이해함 -> 총 일수를 반환하는거지, 가능한 첫 날짜라고 생각함.
def solution(want, number, discount):
    
    # 딕셔너리 생성
    want_dic = {x:num for x,num in zip(want,number)}
    
    for i in range(len(discount)):
        dic = want_dic.copy() #copy가 아니면 본 객체를 참조해서 같이 값이 변화됨
        # 10 이상
        if(i<=len(discount)-10):
            for j in discount[i:i+10]:
                if j in dic:
                    dic[j]-=1
        # 10 이하        
        else:
            for j in discount[i:]:
                if j in dic:
                    dic[j]-=1
    
        #다 0이라면 return
        for v in dic.values():
            if v>0:
                break
        else:
            return i+1
    
    return 0


# 내 코드로 고치면 
def solution(want, number, discount):
    
    want_dic = {x: num for x, num in zip(want, number)}
    
    result = 0  
    
    for i in range(len(discount) - 9): 
        dic = want_dic.copy()
        
        for j in discount[i:i+10]:
            if j in dic:
                dic[j] -= 1
        
        all_satisfied = True
        for v in dic.values():
            if v > 0:
                all_satisfied = False
                break
        
        if all_satisfied:
            result += 1  
    
    return result

# 실제 정답 
# 딕셔너리를 만들어서 같으면 answer +=1 하는 방식     
def solution(want,number, discount):

    want_dict={}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    for i in range(len(discount)-9):
        discount_10d = {}

        for j in range(i,i+10):
            if discount[j] in want_dict:
                discount_10d[discoint[j]] = discount_10d.get(discount[j],0)+1 #해당 제품이 딕셔너리에 있으면 현재 개수 반환, 없으면 0반환 
        
        if discount_10d == want_dict:
            answer+=1
        
        return answer