def solution(a, b, n):
    answer = 0
    now = n
    while now // a != 0:
        answer += ((now // a) * b)
        now = ((now // a) * b) + (now % a)
    return answer