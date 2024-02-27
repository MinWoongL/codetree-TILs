import sys

input = sys.stdin.readline

n, m = map(int, input().split())
adjL = [[] for _ in range(n + 1)]

for _ in range(m):
    s, g = map(int, input().split())
    adjL[s].append(g)

ans = []
max_cnt = 0

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    cnt = 1
    stack = [i]
    visited[i] = 1
    while stack:
        now = stack.pop()

        for node in adjL[now]:
            if not visited[node]:
                stack.append(node)
                cnt += 1
                visited[node] = 1

    if cnt == max_cnt:
        ans.append(i)
    elif cnt > max_cnt:
        ans = [i]
        max_cnt = cnt
    else:
        continue
ans.sort()
print(*ans)