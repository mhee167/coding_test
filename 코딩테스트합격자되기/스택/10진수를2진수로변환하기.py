number = int(input())
result_list = []
original_number = number
while not number < 2:
    result_list.append(number%2)
    number = number//2

result_list.append(number)

while result_list:
    print(result_list.pop(),end="")