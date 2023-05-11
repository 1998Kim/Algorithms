def solution(babbling):
    answer = 0
    can_words = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        back = ''
        while word:
            first = word[0]
            if first == 'a' or first == 'w':
                if word[0:3] in can_words and back != first:
                    back = first
                    word = word[3:]
                else:
                    break
            elif first == 'y' or first == 'm':
                if word[0:2] in can_words and back != first:
                    back = first
                    word = word[2:]
                else:
                    break
            else:
                break
        if len(word) == 0:
            answer += 1
    return answer