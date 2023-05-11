# 글자를 읽음
# 첫 글자 등장 수와 다른 글자 수가 같을 때 멈춤 => 문자열 자름
# 자른 문자열 갯수 반환
def solution(s):
    answer = 0
    same_cnt = 0
    diff_cnt = 0
    first_str = s[0]
    
    while s:
        now = s[0]
        if first_str == now:
            same_cnt += 1
        elif first_str != now:
            diff_cnt += 1
        
        if same_cnt == diff_cnt:
            answer += 1
            same_cnt = 0
            diff_cnt = 0
            if len(s) > 1:
                first_str = s[1]
        s = s[1:]

    if same_cnt != diff_cnt: # cnt 두 변수의 값이 다른데 더 이상 읽을 글자가 없는 경우 대비
        answer += 1
    return answer