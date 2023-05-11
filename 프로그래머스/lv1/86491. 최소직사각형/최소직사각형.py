def solution(sizes):
    answer = 0
    long = []
    short = []
    for i in sizes:
        long.append(max(i[0], i[1]))
        short.append(min(i[0], i[1]))
        # print(i[0], i[1])
    answer = max(long) * max(short)

    return answer