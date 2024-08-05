import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(100)]

    di= [0]
    dj= [1]

    len_result = 0
    mx_result = 0

    i,j = 0,0

    for k in range(0):
        result = []
        for l in range(100):
            ni = i + di[k] * l
            nj = j + dj[k] * l
            result += arr[ni][nj]

            if result == result[::-1]:
                len_result = len(result)

            if mx_result < len(result):
                mx_result = len_result
    print(mx_result)
