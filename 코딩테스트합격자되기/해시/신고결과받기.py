#내 풀이
def solution(id_list, report, k):
    answer_list = []
    id_dic = {x:set() for x in id_list}
    id_dic2 = {x:0 for x in id_list}
    # 각 아이디별 신고 횟수 저장
    for i in range(len(report)):
        individual_report = report[i].split(" ")
        id_dic[individual_report[0]].add(individual_report[1])
    # 아이디별 리포트 받는 횟수 출력.
    for i in id_dic.keys():
        for id in id_dic[i]:
            id_dic2[id]+=1
    for i in id_dic.keys():
        answer=0
        for id in id_dic[i]:
            if id_dic2[id]>=k:
                answer+=1
        answer_list.append(answer)
    return answer_list

#정답
# 나랑 다른 관점으로 딕셔너리 저장 -> 딕셔너리 문제에서 나랑 관점이 다르면 반대로 키,값 저장해보기!
def solution(id_list, report,k):
    reported_user= {} #신고당한 유저
    count={} #각 유저가 받을 메일 개수

    # 신고당한 유저별로 신고한 유저 저장
    # 신고당한 유저만 저장하기 때문에 더 효율적! 
    for r in report:
        user_id, reported_id = r.split()
        if reported_id not in reported_user:
            reported_user[reported_id] = set()
        reported_user[reported_id].add(user_id)

    for reported_id, user_id_lst in reported_user.items():
        if len(user_id_lst) >=k: #k번 이상이면
            for uid in user_id_lst:
                if uid not in count:
                    count[uid]=1
                else:
                    count[uid]+=1
    answer=[]

    for i in range(len(id_list)):
        if id_list[i] not in count:
            answer.append(0)
        else:
            answer.append(count[id_list[i]])
    #이렇게 가능
    # for uid in user_id_lst:
    #   count[uid]= count.get(uid,0)+1 #실행이 반복될때마다 값이 1 더해짐
    return answer