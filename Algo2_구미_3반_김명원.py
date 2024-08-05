T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 경사도 길이 구분하기

    arr_index = []
    for j in range(1, N):
        if arr[j - 1] > arr[j]:
            arr_index.append(j)
    # 인덱스 시작점 추가
    arr_index.append(0)
    # 인덱스 끝점 추가
    arr_index.append(len(arr))
    # 순서대로 정렬
    arr_index.sort()
    # mn_result = 최소 경사로 출력
    mn_result = 9999999
    # mn_result의 결가값이 최소 일때 result 길이를 len_result에 저장
    len_result = 0
    for k in range(1, len(arr_index)):
        result = []
        mx_arr = 0
        mn_arr = 9999
        for l in range(arr_index[k - 1], arr_index[k]):
            result.append(arr[l])
        # 최대 최소 구하기
        for i in range(len(result)):

            if mx_arr < result[i]:
                mx_arr = result[i]

            if mn_arr > result[i]:
                mn_arr = result[i]

        # 경사도가 영어로 몰라서 deep으로 함

        deep = (mx_arr - mn_arr) / len(result)
        # 만약 deep이 0이라면 지나치기
        if deep == 0:
            continue

        if mn_result > deep:
            mn_result = deep
            len_result = len(result)

        # mn_result와 deep이 같다면 길이가 더 긴 것을 저장 어쩌피 mn_result의 값은 부동소수점 에러를 상관 안쓰기 때문에 같음
        elif mn_result == deep:
            if len_result > len(result):
                len_result = len_result
            else:
                len_result = len(result)

    print(f'#{tc} {len_result}')
