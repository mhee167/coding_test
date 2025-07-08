string_list = list(input().split(","))
query_list = list(input().split(","))

string_dic = {x:x for x in string_list}

result_list=[]
for i in query_list:
    if string_dic.get(i):
        result_list.append("True")
    else:
        result_list.append("False")

#정답

#기존의 문자열 해싱 -> 아스키코드값 * 31의 거듭제곱 형태 % 버킷크기 
# 호너의 방법 사용 -> 거듭제곱을 어떻게 계산하느냐의 차이
def polynomial_hash(str):
    p=31
    m=1000000007 #버킷크기
    hash_value=0
    for char in str:
        hash_value = (hash_value*p + ord(char))% m
    return hash_value

# 정답 
def solution(string_list, query_list):
    hash_list = [polynomial_hash(str) for str in string_list]

    result=[]
    for query in query_list:
        query_hash = polynomial_hash(query)
        if query_hash in hash_list:
            result.append(True)
        else:
            result.append(False)
    return result