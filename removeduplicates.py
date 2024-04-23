def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j

nums = [1, 1, 2, 2, 3, 4, 4, 4, 5]
print(removeDuplicates(nums))  

