T = int(input())

for tc in range(1, T+1):

    N = list(input())
    M = list(input())

    N_dict = {}

    for i in N:
        N_dict[i] = 0

    for j in M:
        if j not in N_dict.keys():
            continue
        else:
            N_dict[j] += 1

    mx_result = max(N_dict.values())

    print(f'#{tc} {mx_result}')