def collatz(k):
    temp = [k]
    
    while k != 1:
        if k%2 == 0:
            k = k // 2
        else:
            k = k * 3 +1
        temp.append(k)
    
    return temp, len(temp)


def intergral(coords):
    temp = []

    for index in range(len(coords)-1):
        y1, y2 = coords[index], coords[index+1]
        temp.append(min(y1,y2) + abs(y2-y1) / 2)
    
    return temp


def solution(k, ranges):
    answer = []
    coords, n = collatz(k)
    areas = intergral(coords)

    for sample in ranges:
        a, b = sample
        x1, x2 = a, n + b
        
        if x1 >= x2:
            answer.append(-1)
        else:
            area = 0
            for index in range(x1, x2-1):
                area += areas[index]
            answer.append(area)
    
    return answer