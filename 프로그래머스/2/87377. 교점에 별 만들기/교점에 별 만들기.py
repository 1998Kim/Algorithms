def solution(line):
    coords = []
    max_x, min_x, max_y, min_y = float('INF')*(-1), float('INF'), float('INF')*(-1), float('INF')
    
    for index in range(len(line)-1):
        a, b, c = line[index]
        for index_next in range(index+1, len(line)):
            d, e, f = line[index_next]

            if (a*e - b*d) == 0:
                continue
            x = (b*f - c*e) / (a*e - b*d)
            y = (c*d - a*f) / (a*e - b*d)
            if x == int(x) and y == int(y) and (int(x), int(y)) not in coords:
                coords.append((int(x), int(y)))
                max_x = max(max_x, int(x))
                min_x = min(min_x, int(x))
                max_y = max(max_y, int(y))
                min_y = min(min_y, int(y))

    coords.sort(key=lambda x: (x[1], x[0]), reverse=True)
    answer = [['.' for _ in range(max_x - min_x+1)] for _ in range(max_y - min_y+1)]
    
    for x, y in coords:
        answer[max_y-y][x-min_x] = '*'
    return [''.join(temp) for temp in answer]