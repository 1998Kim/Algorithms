def solution(n):
    answer = list(map(int, list(str(n))))
    answer.sort(reverse=True)
    answer = ''.join(list(map(str, answer)))
    return int(answer)