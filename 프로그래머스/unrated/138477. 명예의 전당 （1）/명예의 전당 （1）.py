# score에는 각 날에 가수의 점수가 있음
# 점수가 상위 k번째 이면 명예의 전당에 기록
# 명예의 전당 최하위 점수 발표
def solution(k, score):
    answer = []
    honor = []

    for i in score:
        if len(honor) < k:
            honor.append(i)
            honor.sort()
            answer.append(honor[0])
        else:
            honor.append(i)
            honor.sort()
            honor = honor[1:]
            answer.append(honor[0])

    # print('answer', answer)
    return answer