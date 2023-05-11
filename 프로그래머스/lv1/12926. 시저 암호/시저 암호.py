def solution(s, n):
    answer = ''

    # print(chr(96))
    # print(ord('a'), ord('A')) #97 65
    # print(ord('z'), ord('Z')) #122 90

    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if 65 <= ord(i) <= 90: #대문자
                if 65 <= (ord(i)+n) <= 90:
                    answer += chr(ord(i)+n)
                else: # 범위 벗어남
                    answer += chr(ord(i) + n - 26)
            if 97 <= ord(i) <= 122: #소문자
                if 97 <= (ord(i)+n) <= 122:
                    answer += chr(ord(i)+n)
                else: # 범위 벗어남
                    answer += chr(ord(i) + n - 26)

    return answer