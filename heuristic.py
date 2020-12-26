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

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.x == other.x and self.y == other.y)

def heuristic(queen, arranged_queens):
    for q in arranged_queens:
        if queen.can_attack(q):
            return 1
    return 0


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
            if L in results:
                break
            reserve_L = [Queen(q.x,(N-1) - q.y) for q in L.copy()]
            results.append(L)
            results.append(reserve_L)

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