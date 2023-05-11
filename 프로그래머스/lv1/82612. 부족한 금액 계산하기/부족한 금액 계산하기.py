def solution(price, money, count):
    answer = -1
    total_money = 0
    for i in range(1, count+1):
        total_money += price * i
    if total_money > money:
        answer = total_money - money
    else:
        answer = 0
    return answer