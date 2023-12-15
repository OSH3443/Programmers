def solution(x, y):
    answer = ""
    for num in range(9,-1,-1):
        answer += (str(num) * min(x.count(str(num)),y.count(str(num))))
    if answer == '':
        return "-1"
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer