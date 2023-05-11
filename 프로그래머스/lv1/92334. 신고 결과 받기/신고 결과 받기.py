# 각 유저는 타 유저 신고가능, 횟수제한 X   단, 동일 유저를 여러번 신고해도 1회 신고로 간주
# k번 이상 신고된 유저는 이용 정지
# 이용정지된 유저를 신고한 유저에게 정지메일감

def solution(id_list, report, k):
    answer = []
    
    report_num = dict.fromkeys(id_list, 0) # 각 유저의 id가 key로 들어간 사전
    id_report = dict.fromkeys(id_list)
    
    for i in report:
        a = i.split()[0] # 신고한 유저
        b = i.split()[1] # 신고당한 유저
        
        value = id_report[a]
        if value == None:
            value = []
    
        if b not in value:
            value.append(b)
            id_report.update({a: value})
            report_num[b] += 1

    stop_id = []
    for key, value in report_num.items():
        if value >= k:
            stop_id.append(key)
            
    for key, values in id_report.items():
        mail_num = 0
        if values is not None:
            for value in values:
                if value in stop_id:
                    mail_num += 1
        answer.append(mail_num)
    return answer