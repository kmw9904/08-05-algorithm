T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    mx_result = 0
    for i in range(N):
        for j in range(N):
            result = 0
            result += arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < N:
                    result += arr[ni][nj]

            if result <= 0:
                result = - result
                if mx_result > result:
                    mx_result = -result

            if mx_result < result:
                mx_result = result

    print(f'#{tc} {mx_result}')
