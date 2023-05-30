# 이진수변환
import sys

n = int(sys.stdin.readline())
# print(n)

answer = ''

while n:
    n, rest = divmod(n, 2)
    answer += str(rest)
print(answer[::-1])