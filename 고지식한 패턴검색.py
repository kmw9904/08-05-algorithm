def f(t,p):     # 패턴 p와 일치하는 구간의 시작인덱스 리턴, 일치하는 경우가 없으면 -1 리턴
    N = len(t)
    M = len(p)

    for i in range(N-M+1):
        for j in range(M):
            if t[i + j] != p[j]:
                break
        else:
            return i # 패턴을 찾은 경우
    return -1



t = 'TTTTTTTATTTAATA'
p = 'TTA'
print(f(t, p))