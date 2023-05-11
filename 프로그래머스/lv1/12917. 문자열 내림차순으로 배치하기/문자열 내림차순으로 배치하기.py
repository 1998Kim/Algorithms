def solution(s):
    answer = ''
    list_s = list(s)
    list_s.sort(reverse=True)
    # print(list_s)
    answer = ''.join(c for c in list_s)

    return answer