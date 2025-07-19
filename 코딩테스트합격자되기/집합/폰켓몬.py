
def solution(nums):
    number = len(set(nums))
    pick_number = len(nums)//2
    
    if(pick_number>=number):
        return number
    else:
        return pick_number
        

#정답
def solution(nums):
    num_set = set(nums)
    n=len(nums)
    k=n//2
    return min(k,len(num_set))