def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

nums = [2,7,13,15,19]
target = 15
print(two_sum(nums, target))

#output : [0, 2]