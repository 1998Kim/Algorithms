def solution(numbers):
    sample = list(range(10))
    
    for i in numbers:
        if i in sample:
            sample.remove(i)
    answer = sum(sample)
    return answer