def solution(cards1, cards2, goal):
    cnt = 0
    for i in range(len(goal)):
        now_goal = goal[i]
        if len(cards1) != 0:
            if cards1[0] == now_goal:
                cnt += 1
                del cards1[0]
        if len(cards2) != 0:
            if cards2[0] == now_goal:
                cnt += 1
                del cards2[0]

    if cnt == len(goal):
        answer = 'Yes'
    else:
        answer = 'No'
    return answer