number = int(input())
result_list = []
original_number = number
while not number < 2:
    result_list.append(number%2)
    number = number//2

result_list.append(number)

while result_list:
    print(result_list.pop(),end="") #출력 후 끝에 붙이는 문자


#정답 -> 문자열로 저장함.
def solution(decimal):
    stack=[]
    while decimal >0:
        remainder = decimal %2
        stack.append(str(remainder))
        decimal //= 2
    while stack:
        binary += stack.pop() #+= 연산자는 수행할때마다 객체를 새로 생성함. 
    return binary 