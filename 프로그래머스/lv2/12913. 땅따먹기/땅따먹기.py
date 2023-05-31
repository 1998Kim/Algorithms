def solution(land):
    answer = 0
    y = len(land)
    # print(y)
    for idy in range(y-1):
        sort_land = sorted(land[idy])
        first_num = sort_land[-1]  # 최댓값
        second_num = sort_land[-2] # 다음 최댓값
        # print(idy)
        if first_num == second_num:
            for idx in range(4):
                land[idy+1][idx] += first_num
        else:
            for idx in range(4):
                if land[idy][idx] != first_num:
                    land[idy+1][idx] += first_num
                else:
                    land[idy+1][idx] += second_num
    # print(max(land[y-1]))
    answer = max(land[y-1])
    return answer