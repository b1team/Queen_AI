import time

class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def can_attack(self, other):
        if self.y == other.y:
            return True
        if abs(self.x - other.x) == abs(self.y - other.y):
            return True
        return False


def heuristic(queen, arranged_queens):
    for q in arranged_queens:
        if queen.can_attack(q):
            return 1
    return 0


def find_half(res, N):
  results, ls = [], []
  for pos in res:
    for q in pos:
      queen = Queen(q.x, (N-1) - q.y)
      ls.append(queen)
  results.append(ls)

  return results


def get_queen_position(N):
    OPEN = [Queen(0, i) for i in range(N)]
    L = []
    results = []
    while True:
        if len(OPEN) == 0:
            break
        u = OPEN.pop(0)
        L = L[:u.x]
        L.append(u)
        if u.x < (N - 1):
            for y in range(N):
                if y == u.y - 1 or y == u.y or y == u.y + 1:
                    continue
                v = Queen(u.x + 1, y)
                if heuristic(v, L) == 0:
                    OPEN.insert(0, v)
        else:
            results.append(L)

            if N % 2 == 0:
              if u.x == N // 2:
                half = find_half(results, N)
                results.extend(half)
            else:
              if u.x == ((N//2) + 1):
                half = find_half(results[:-1], N)
                results.extend(half)

    return results


def solve():
    N = int(input("NHAP N: "))
    start = time.time()
    results = get_queen_position(N)
    end = time.time()
    # print([[(i.x, i.y) for i in res] for res in results])
    print("LEN: ", len(results))
    print("DONE IN: ", end - start, "s")


if __name__ == "__main__":
    solve()