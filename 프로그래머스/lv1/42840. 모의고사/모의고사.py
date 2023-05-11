def solution(answers):
    answer = []
    check = [0, 0, 0]
    num_1 = list(range(1,6)) # 길이 5
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5] # 길이 8
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 길이 10

    for i in range(len(answers)):
        if answers[i] == num_1[i % 5]:
            check[0] += 1
        if answers[i] == num_2[i % 8]:
            check[1] += 1
        if answers[i] == num_3[i % 10]:
            check[2] += 1

    for index, value in enumerate(check):
        if value == max(check):
            answer.append(index+1)

    return answer