def solution(a, b):
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = sum(days[:a-1]) + b
    answer = week[total_day % 7]
    return answer