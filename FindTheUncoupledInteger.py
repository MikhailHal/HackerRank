nums = list(map(int, input().split(",")))
ans = nums[0]
for i in range(1, len(nums)):
    ans = ans ^ nums[i]
print(ans)