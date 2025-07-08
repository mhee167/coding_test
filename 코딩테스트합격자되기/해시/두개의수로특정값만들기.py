arr = list(map(int,input().split(",")))
target= int(input())


def solution(arr, target):
    multiple= {x: x for x in arr}
    for i in multiple:
        if (multiple.get(target-i) and target-i != i):
            return True
    else:
        return False

print(solution(arr,target))


#정답 

#배열 크기의 해시테이블을 미리 생성
# 각 숫자가 존재하는지 1/0으로 표시
def count_sort(arr,k):
    hashtable = [0]*(k+1)

    for num in arr:
        if num<=k:
            hashtable[num]=1
    return hashtable

def solution(arr,target):
    hashtable = count_sort(arr,target)

    for num in arr:
        complement = target-num
        if(complement != num and complement >=0 and complement <= target and hashtable[complement] ==1):
            return True
    return False