import sys
from datetime import datetime
input = sys.stdin.readline

s, e, q = input().split()
s = datetime.strptime(s, "%H:%M")
e = datetime.strptime(e, "%H:%M")
q = datetime.strptime(q, "%H:%M")

cond1 = {}
cond2 = {}
N = int(input())

for _ in range(N):
    t, stu = input().split()
    t = datetime.strptime(t, "%H:%M")

    if stu not in cond1.keys():
        cond1[stu] = 0
    
    if stu not in cond2.keys():
        cond2[stu] = 0

    if t <= s:
        cond1[stu] = 1
    
    if e <= t <= q:
        cond2[stu] = 1

cnt = 0
for stu in cond2.keys():
    if cond2[stu] and cond1[stu]:
        cnt += 1
    
print(cnt)