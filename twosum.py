class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for index,num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff],index]
            num_map[num] = index
        return []

sol = Solution()
nums = input()
nums = nums.strip('[]')
nums = nums.split(',')
nums = [int(i) for i in nums]
target = int(input())
result = sol.twoSum(nums,target)
print(result)