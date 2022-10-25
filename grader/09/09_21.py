def factor(N):
    factors = []
    while True:
        if N == 1:
            break
        for i in range(2, N+1):
            if N % i == 0:
                factors.append([i, 0])
                while True:
                    if N % i == 0:
                        N //= i
                        factors[-1][1] += 1
                    else:
                        break

    return factors


exec(input().strip())
