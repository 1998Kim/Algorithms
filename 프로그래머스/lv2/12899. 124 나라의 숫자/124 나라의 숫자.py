# 3진법과 유사
# 다른점: 0,1,2 -> 1,2,4
def solution(n):
    answer = ''
    # print(divmod(n,3))
    while n:
        n, rest = divmod(n,3)
        if rest == 0:
            n -= 1
            answer += '4'
        else:
            answer += str(rest)
    print(answer, "".join(reversed(answer)))
    return answer[::-1]