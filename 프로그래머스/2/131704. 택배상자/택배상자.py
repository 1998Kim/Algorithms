def solution(order):
    answer = 0
    
    truck, sub, index, box = [], [], 0, 1
    
    while True:
        if box <= len(order):
            if order[index] == box:
                truck.append(box)
                index += 1
            else:
                sub.append(box)
            box += 1

        if len(sub) != 0 and sub[-1] == order[index]:
            truck.append(sub[-1])
            del sub[-1]
            index += 1
        elif box > len(order):
            break
            
    answer = len(truck)
    return answer