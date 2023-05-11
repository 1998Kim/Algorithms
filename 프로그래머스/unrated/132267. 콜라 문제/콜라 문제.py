# 빈병 a개를 가져다 주면 b병을 줌
# 전체 병이 n개 일 때 총 몇병을 받을 수 있는지

def solution(a, b, n):
    answer = 0
    while n >= a:
        mod, rest = divmod(n, a)
        answer += mod * b
        n = mod * b + rest
    return answer