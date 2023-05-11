# 문자열 s의 각 글자를 index만큼 뒤의 껄로 바꿈
# 이때 skip에 있는 알파벳은 제외함, 모든문자는 소문자
def solution(s, skip, index):
    answer = ''
    ord_skip = [ord(s) for s in skip] # skip할 문자의 아스키코드 값이 들어있음
    ord_skip.sort()
    # print(ord('a'), ord('z')) # 97 122
    print(skip, ord_skip)
    # for j in range(1, index+1):
    #     print(j) # 1~5
    for i in s:
        # print(i, ord(i), ord(i) + index, chr(ord(i) + index))
        ord_now = ord(i)
        for j in range(1, index+1):
            ord_now += 1
            if ord_now > 122:
                ord_now = 97
            while ord_now in ord_skip:
                ord_now += 1
                if ord_now > 122:
                    ord_now = 97
            if ord_now > 122:
                ord_now = 97
        answer += chr(ord_now)
#        print(chr(ord_now))
    return answer