# 팩토리얼
import sys


def factorial(num, answer):
    if num == 0:
        print(answer)
        return
    else:
        answer *= num
        factorial(num-1, answer)
        

n = int(sys.stdin.readline())
# print(n)

factorial(n, 1)