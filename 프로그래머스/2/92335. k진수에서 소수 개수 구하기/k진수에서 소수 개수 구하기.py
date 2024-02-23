def change(n, k):
    k_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5' , 6: '6', 7: '7', 8: '8', 9: '9'}
    p = ''
    
    while n > 0:
        n, rest = divmod(n, k)
        p += k_dict[rest]
    
    return p[::-1]

def solution(n, k):
    answer = 0

    n_k = change(n, k)
    for p in n_k.split('0'):
        if p == '' or p == '1':
            continue
        p = int(p)
        prime = True
        for i in range(2, int(p**(0.5))+1):
            if p % i == 0:
                prime = False
                break
        if prime:
            answer += 1
    return answer