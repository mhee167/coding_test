gualho_list = list(input())
result_list = []
for gualho in gualho_list:
    if gualho == "(":
        result_list.append(gualho)
    else:
        if len(result_list)>0: 
            result_list.pop()
        else:
            result_list.append(gualho)

print(len(result_list)==0)


def solution(s):
    stack=[]
    for c in s:
        if c == "(":
            stack.append(c)
        elif c==")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return True
    else:
        return False