def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    answer = 0
    
    for idx in range(len(A)):
        answer += A[idx] * B[idx]

    return answer