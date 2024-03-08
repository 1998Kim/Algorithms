import heapq

def solution(n, k, enemy):
    answer = 0
    queue = []
    
    for index, num in enumerate(enemy):
        heapq.heappush(queue, num)
        
        if len(queue) > k:
            n -= heapq.heappop(queue)
        if n < 0:
            return index
    
    return len(enemy)