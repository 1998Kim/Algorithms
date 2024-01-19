# N개의 수의 최소공배수 계산
# 각 수를 소인수분해 -> 약수의 최댓값으로 최소공배수 계산

def solution(arr):
    answer = 1
    total_div = {} # dict 선언

    for num in arr:
        if num == 1: # 1은 약수 구할 필요 X
            continue
        
        # 소인수분해 진행
        num_div = 2
        num_prime = {}
        while num != 1:
            if num % num_div == 0:
                num = num // num_div
                if num_div not in num_prime.keys():
                    num_prime[num_div] = 1
                else:
                    num_prime[num_div] += 1
            else:
                num_div += 1
    
        for num_key, num_value in num_prime.items():
            if num_key not in total_div.keys():
                total_div[num_key] = num_value
            else:
                if total_div[num_key] < num_value:
                    total_div[num_key] = num_value

    for total_key, total_value in total_div.items():
        answer = answer * (total_key**total_value)
    return answer