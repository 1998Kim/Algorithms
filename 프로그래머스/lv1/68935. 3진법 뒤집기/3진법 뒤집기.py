def solution(n):
    answer = 0
    result = ''
    # 3진법 변환
    # 원래는 뒤집어야지 완성되나 문제에서 뒤집은 수의 10진수 표현 구하기임
    while n:
        result += str(n % 3)
        n = n // 3
    answer = int(result, 3)
    return answer