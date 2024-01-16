import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
for i in range(N, 1, -1):
    for j in range(i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
    print(*numbers)