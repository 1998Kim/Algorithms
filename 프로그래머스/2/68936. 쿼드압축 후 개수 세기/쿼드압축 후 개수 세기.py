from itertools import product

def solution(arr):
    n_dict = {2**i: i for i in range(11)}
    n = n_dict[len(arr)]
    
    total_area = 0
    for y in range(len(arr)):
        total_area += sum(arr[y])
    
    if (2**n) == (total_area**0.5):
        if total_area == 0:
            return [1, 0]
        else:
            return [0, 1]

    for i in range(n-1, 0, -1):
        s = 2**i 
        i_coords = []

        for x in range(s-1, len(arr), s):
            for y in range(s-1, len(arr), s):
                i_coords.append((x, y))

        for i_coord in i_coords:
            x, y = i_coord
            area = 0
            change_state = False

            for y_index in range(y-s+1, y+1):
                area += sum(arr[y_index][x-s+1:x+1])
            if area == s**2 or area == 0:
                change_state = True

            if change_state:
                for y_index in range(y-s+1, y+1):
                    arr[y_index][x-s+1:x+1] = [-1] * s
                arr[y][x] = area // (s**2)
    
    num_zero, num_one = 0, 0
    for y in range(len(arr)):
        num_zero += arr[y].count(0)
        num_one += arr[y].count(1)
    answer = [num_zero, num_one]
    return answer