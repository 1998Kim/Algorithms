def solution(n, m):
    for i in range(min(n, m) ,0 , -1):   # 최대 공약수
        if n % i == 0 and m % i == 0:
            max_num = i
            break

    for j in range(max(n, m), n*m+1, 1): # 최소 공배수
        if j % n == 0 and j % m == 0:
            min_num = j
            break
    answer = [max_num, min_num]

    return answer