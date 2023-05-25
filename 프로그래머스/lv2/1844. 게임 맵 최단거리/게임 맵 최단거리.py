# 벽(0) -> 갈 수 없음, 정해진 길(1)이 있음
# 이동은 동서남북 한 칸씩가능
# 최단 경로 구하기 경로가 없으면 -1
# 초기 위치 : 좌상단(내가 시작) 우하단(상대 : 목표)
from collections import deque

def solution(maps):
    x, y = len(maps[0]), len(maps)
    check_maps = [[False for _ in range(x)] for _ in range(y)]# 간 적이 있는지 없는지 체크
    cnt_maps = [[-1 for _ in range(x)] for _ in range(y)]     # 경로(칸 수)를 체크
    cnt_maps[0][0] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    Queue = deque()
    Queue.append([0, 0])

    while Queue:
        now_x, now_y = Queue.popleft()
        
        # print('now', now_x, now_y)
        
        for idx in range(4):
            new_x, new_y = now_x + dx[idx], now_y + dy[idx]
            # 다음 좌표가 갈 수 있는지 없는지 체크
            if 0 <= new_x < x and 0 <= new_y < y and maps[new_y][new_x] == 1:  
                if check_maps[new_y][new_x] == False and cnt_maps[new_y][new_x] == -1:
                    check_maps[new_y][new_x] = True
                    cnt_maps[new_y][new_x] = cnt_maps[now_y][now_x] + 1
                    Queue.append([new_x, new_y])
    # print(check_maps)
    return cnt_maps[-1][-1]