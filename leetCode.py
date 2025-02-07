nums = list(map(int, input().split()))
result = [nums[nums[i]] for i in range(len(nums))]
sorted_result = sorted(result)
print(sorted_result)
