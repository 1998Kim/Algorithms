def solution(s):
    answer = []
    s_list = s[1:-1].replace('{', '').replace('}', ' ').split(' ')
    s_list.sort(key=len)
    news = []

    for now in s_list:
        if now == '':
            continue
        temp = []
        for i in now.replace(',', ' ').split(' '):
            if i != '':
                temp.append(int(i))
        news.append(temp)
        
    for new in news:
        for num in new:
            if num not in answer:
                answer.append(num)
        
    return answer