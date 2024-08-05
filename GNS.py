import sys

sys.stdin = open('GNS_test_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = input().split()
    arr = list(input().split())
    arr_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    arr_dict = {}
    for i in arr_lst:
        arr_dict[i] = 0

    for j in arr:
        arr_dict[j] += 1

    result = []

    print(f'#{tc}')
    for k in arr_lst:
        for l in range(arr_dict[k]):
            print(k , end=' ')

