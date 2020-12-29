import time
a = [-1 for _ in range(20)]
results = []


def Ok(x, y):
    for i in range(1, x):
        if a[i] == y or abs(i - x) == abs(a[i] - y):
            return False
    return True


def get_position(N):
    ls = []
    for i in range(1, N+1):
        ls.append(a[i])

    return ls


def Try(i, N):
    for j in range(1, N+1):
        if Ok(i, j):
            a[i] = j
            if i == N:
                pos = get_position(N)
                results.append(pos)
            Try(i+1, N)


if __name__ == "__main__":
    N = int(input('Nhap N: '))
    start = time.time()
    Try(1, N)
    end = time.time()
    # print(results)
    print('LEN: ', len(results))
    print('Time:', end-start)
