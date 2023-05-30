# 카드2
# N장의 카드 존재 처음엔 카드 버림, 다음엔 제일 위에 있는 카드를 아래에 놓음 -> N = 1일 때까지 반복
import sys
from collections import deque

N = int(sys.stdin.readline())
# print(N, type(N))

Queue = deque()

for i in range(1, N+1):
    Queue.append(i)

# print(Queue)

cnt = 0

while len(Queue) != 1:
    num = Queue.popleft()
    if cnt % 2 == 1:
        Queue.append(num)
    cnt += 1

print(Queue[0])
