import sys

nums = []
for line in sys.stdin:
    nums.append(int(line.strip()))
maxNum = max(nums)
dp = [-1] * (maxNum+1)
for i in range(maxNum+1):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

for num in nums:
    print(dp[num])