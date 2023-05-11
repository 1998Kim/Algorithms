def solution(nums):
    take_num = int(len(nums) / 2)
    unique_num = len(set(nums))
    print(take_num, unique_num)
    if take_num > unique_num:
        answer = unique_num
    else:
        answer = take_num
    return answer