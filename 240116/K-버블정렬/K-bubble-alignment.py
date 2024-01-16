import sys
N, K = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(N-1, N-K-1, -1):
    for j in range(i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(*nums)