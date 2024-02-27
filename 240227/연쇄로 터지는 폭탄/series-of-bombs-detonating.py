import sys
input = sys.stdin.readline


def bt(left, right, score, R):
    global ans
    if not left and not right:
        if score > ans:
            ans = score
        return

    if left:
        m_r = max(0, left - R)
        tmp = []
        for i in range(m_r, left):
            if i in bombs:
                tmp.append(i)
                score = score + 1
        if tmp:
            left = min(tmp)
        else:
            left = False
    if right:
        M_r = min(1000000000, right + R)
        tmp = []
        for i in range(right + 1, M_r + 1):
            if i in bombs:
                tmp.append(i)
                score = score + 1
        if tmp:
            right = max(tmp)
        else:
            right = False

    bt(left, right, score, R + 1)


N = int(input())

bombs = []
for _ in range(N):
    bombs.append(int(input()))

ans = 0

for b in bombs:
    bt(b, b, 1, 1)

print(ans)