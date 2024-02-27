from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    max_cnt = len(queue1) * 4 - 1
    total1 = sum(queue1)
    total2 = sum(queue2)
    
    if (total1 + total2) % 2 != 0:
        return -1
    
    while True:
        if total1 > total2:
            now = queue1.popleft()
            queue2.append(now)
            total1 -= now
            total2 += now
            answer += 1
        elif total1 < total2:
            now = queue2.popleft()
            queue1.append(now)
            total1 += now
            total2 -= now
            answer += 1
        else:
            break
            
        if answer == max_cnt:
            answer = -1
            break

    return answer