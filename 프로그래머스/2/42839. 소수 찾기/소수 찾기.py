from itertools import combinations
from itertools import permutations

def solution(numbers):
    answer = 0
    prime_nums = []
    nums = []
    for num in range(1, len(numbers) + 1):
        for i in set(permutations(numbers, num)):
            nums.append(int(''.join(i)))

    nums.sort()
    
    for num in nums:
        if num < 2:
            continue
        prime_check = True
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                prime_check = False
                break
        if prime_check and num not in prime_nums:
            prime_nums.append(num)
            
    answer = len(prime_nums)
    
    return answer