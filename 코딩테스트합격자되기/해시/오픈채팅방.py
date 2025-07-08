# 내 풀이 

def solution(record):
    answer = []
    result ={}
    result_list=[]
    
    # 이름 확인 
    for item in record:
        name=item.split(" ")
        if name[0]=="Enter":
            result[name[1]]=name[2]
        elif name[0]=="Change":
            result[name[1]]=name[2]

    # 결과 처리         
    for item in record:
        name= item.split(" ")
        if name[0]=="Enter":
            result_list.append(result[name[1]]+"님이 들어왔습니다.")
        elif name[0]=="Leave":
            result_list.append(result[name[1]]+"님이 나갔습니다.")
    return result_list

# 정답

def solution(record):
    answer = []
    uid={}
    for line in record:
        cmd = line.split(" ")
        if cmd[0] != "Leave":
            uid[cmd[1]] = cmd[2]
    for line in record:
        cmd = line.split(" ")
        if cmd[0]=="Enter":
            answer.append("%s님이 들어왔습니다."%uid[cmd[1]])
        elif cmd[0]=="Change":
            pass
        else:
            answer.append("%s님이 나갔습니다."%uid[cmd[1]])
    return answer

    