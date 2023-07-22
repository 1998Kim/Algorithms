def solution(n, words):
    answer = []

    prev_word = words[0]
    check = [prev_word]

    for idx, word in enumerate(words):
        if idx == 0:
            continue
        else:
            if prev_word[-1] != word[0] or word in check:
                answer = [idx % n + 1, (idx // n) + 1]
                break
            prev_word = word
            check.append(word)
    
    if len(answer) == 0: # 탈락자가 없는 경우
        answer = [0, 0]

    return answer