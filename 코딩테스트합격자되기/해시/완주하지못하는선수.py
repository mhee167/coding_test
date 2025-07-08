# 잘못된 경우 -> 키값 때문에 단순 존재 여부만 저장됨(2명 참가해도 1개만 있다고 인식)
# 딕셔너리는 pop이 불가능! 인수 넘겨줘야 함. 
def solution(participant, completion):
    completion_dic = {x:x for x in completion}
    participant_dic = {x:x for x in participant}
    for i in participant:
        if not completion_dic.get(i):
            return i
        else:
            participant_dic.pop(i)
            completion_dic.pop(i)
    return participant_dic.pop()

#정답
def solution(paritipant, completion):
    dic={}

    # 참가자 카운트
    for p in participant:
        if p in dic:
            dic[p]+=1
        else:
            dic[p]=1
    
    # 완주자 카운트 
    for c in completion:
        dic[c]-=1
    
    # 완주하지 못한 선수 return
    for key in dic.keys():
        if dic[key] >0:
            return key
