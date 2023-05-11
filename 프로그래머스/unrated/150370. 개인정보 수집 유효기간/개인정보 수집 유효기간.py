# 개인 정보 n개 + 약관 정보
# 약관 별 보관 유효기간이 다름
# today : 오늘날짜
# terms : 약관 + 유효기간 (약관 : A~Z, 기간(달) : 1이상 ~ 100이하)
# privacies : 수집날짜 + 약관
def solution(today, terms, privacies):
    answer = []
    terms_dict = {} # 약관=key, 기간=value인 사전
    today_y = int(today.split('.')[0])
    today_m = int(today.split('.')[1])
    today_d = int(today.split('.')[2])
    
    # print(today_y, today_m, today_d) # 오늘 날짜 연도, 달, 일 정보가 int형으로 저장
    
    for i in terms:
        terms_dict[i.split()[0]] = int(i.split()[1])
    # print(terms_dict) 
    
    for index, value in enumerate(privacies):
        person_date = value.split()[0]
        person_term = value.split()[1]
        term = terms_dict[person_term]
        term_y, term_m = divmod(term, 12) # 유효기간을 연,달로 구분
        
        person_y = int(person_date.split('.')[0]) # 약관 가입 연도
        person_m = int(person_date.split('.')[1]) # 약관 가입 달
        person_d = int(person_date.split('.')[2]) # 약관 가입 일
        
        check_y = person_y + term_y
        check_m = person_m + term_m
        if check_m > 12:
            check_m -= 12
            check_y += 1
        
        if today_y > check_y:
            answer.append(index+1)
        elif today_y == check_y:
            if today_m > check_m:
                answer.append(index+1)
            elif today_m == check_m:
                if today_d >= person_d:
                    answer.append(index+1) 
        # print('today', today_y, today_m, today_d, end='')
        # print(' person', person_y, person_m, person_d, end='')
        # print(' 만료일', check_y, check_m, person_d)
    return answer