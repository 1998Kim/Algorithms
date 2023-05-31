def solution(n):
    answer = 0
    n_one = bin(n)[2:].count('1') # 2진법 수의 1의 갯수
    # print(n_one)
    for num in range(n+1, n**2):
        num_one = bin(num)[2:].count('1')
        if num_one == n_one:
            answer = num
            break
    return answer