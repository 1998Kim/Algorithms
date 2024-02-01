def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    
    for index in range(len(phone_book)-1):
        if len(phone_book[index]) < len(phone_book[index+1]): # 접두어가 되려면 현재가 다음보다 짧아야함
            if phone_book[index+1][:len(phone_book[index])] == phone_book[index]:
                answer = False
                break

    return answer