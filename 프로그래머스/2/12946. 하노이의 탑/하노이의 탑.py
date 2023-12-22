def hanoi(ans, start, target, middle, n):
    if n == 1:
        ans.append([start, target])
        return
    else:
        hanoi(ans, start, middle, target, n-1)
        hanoi(ans, start, target, middle, 1)
        hanoi(ans, middle, target, start, n-1)
    
def solution(n):
    answer = []
    
    hanoi(answer, 1, 3, 2, n)
    
    return answer