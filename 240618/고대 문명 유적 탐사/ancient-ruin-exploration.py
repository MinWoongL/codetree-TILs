import sys
from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
input = sys.stdin.readline


def rotate(lst, x, y):
    tmp = [[lst[i][j] for j in range(5)] for i in range(5)]

    for i in range(3):
        for j in range(3):
            tmp[x-1+i][y-1+j] = lst[x-1+2-j][y-1+i]

    return tmp


def boom_check(lst):
    visited = [[0] * 5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if not visited[i][j] and lst[i][j] != -1:
                q = deque()
                num = lst[i][j]
                q.append([i, j])
                visited[i][j] = 1
                group = []

                tmp_cnt = 0
                while q:
                    x, y = q.popleft()
                    tmp_cnt += 1
                    group.append([x, y])

                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]

                        if 0 <= nx <= 4 and 0 <= ny <= 4:
                            if lst[nx][ny] == num and not visited[nx][ny]:
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                if tmp_cnt > 2:
                    cnt += tmp_cnt
                    for g in group:
                        lst[g[0]][g[1]] = -1
    return cnt, lst


def phase1(lst):
    ans = 0
    # 행, 열, 회전 수(90, 180, 270)
    ans_rct = [0, 0, 0]
    ans_lst = []
    for r in range(1, 4):
        for c in range(1, 4):
            tmp = [[lst[i][j] for j in range(5)] for i in range(5)]
            for t in range(1, 4):
                tmp = rotate(tmp, r, c)
                b_tmp = [[tmp[i][j] for j in range(5)] for i in range(5)]
                cnt, l = boom_check(b_tmp)

                if cnt > ans:
                    ans = cnt
                    ans_rct = [r, c, 90 * t]
                    ans_lst = l
                elif cnt == ans:
                    if 90*t < ans_rct[2]:
                        ans_rct = [r, c, 90 * t]
                        ans_lst = l
                    elif 90*t == ans_rct[2]:
                        if c < ans_rct[1]:
                            ans_rct = [r, c, 90 * t]
                            ans_lst = l
                        elif c == ans_rct[1]:
                            if r < ans_rct[0]:
                                ans_rct = [r, c, 90 * t]
                                ans_lst = l

    return ans, ans_lst


def phase2(lst, r):
    if not r:
        return lst

    for j in range(5):
        for i in range(4, -1, -1):
            if lst[i][j] == -1:
                if r:
                    lst[i][j] = r.popleft()
                else:
                    break
        if not r:
            break

    return lst


K, M = map(int, input().split())

relic = [list(map(int, input().split())) for _ in range(5)]
remain = deque(map(int, input().split()))

ans_lst = []
ans = 0

while K:
    c, relic = phase1(relic)
    if not c:
        break
    ans += c

    while True:
        relic = phase2(relic, remain)
        c, relic = boom_check(relic)
        if not c:
            break
        ans += c

    K -= 1
    ans_lst.append(ans)
    ans = 0
print(*ans_lst)