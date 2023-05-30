# 올바른 괄호 파악
import sys
from collections import deque
n = int(sys.stdin.readline())
check_list = [sys.stdin.readline().split()[0] for _ in range(n)]
# print(n, type(n))
# print(check_list)

state = True  # True -> Yes 출력, False -> No 출력
for now in check_list:
    if now[0] == ')':  # 무조건 틀린 괄호인 경우
        state = False
    else:
        Queue = deque()
        Queue.append(now[0])
        now = now[1:]
        # print(Queue, len(Queue), now)
        while now:
            check = now[0]

            if check == '(':
                Queue.append(check)
            elif check == ')' and len(Queue) != 0:
                Queue.popleft()
            elif check == ')' and len(Queue) == 0:
                break
            now = now[1:]
        if len(now) == 0 and len(Queue) == 0:
            state = True
        else:
            state = False
    if state:
        print('YES')
    else:
        print('NO')
