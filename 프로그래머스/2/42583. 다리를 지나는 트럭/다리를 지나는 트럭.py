def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    now_weight = 0
    truck_num = 0
    
    while truck_weights:
        out_truck = bridge.pop(0)
        now_weight -= out_truck
        if out_truck != 0:
            truck_num -= 1
        
        now_truck = truck_weights[0]
        
        if now_weight + now_truck <= weight and truck_num < bridge_length:
            truck_num += 1
            bridge.append(now_truck)
            now_weight += now_truck
            del truck_weights[0]
        else:
            bridge.append(0)
        answer += 1

    return answer + len(bridge)