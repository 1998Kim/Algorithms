def solution(s):
    answer = ''
    state_change = True
    for word in s:
        if word == ' ':
            answer += ' '
            state_change = True
        elif word.isdigit():
            state_change = False
            answer += word
        elif state_change:
            answer += word.upper()
            state_change = False
        else:
            answer += word.lower()
    return answer