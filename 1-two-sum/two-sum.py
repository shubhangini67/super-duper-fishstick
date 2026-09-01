class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for index, number in enumerate(nums):
            complement = target - number

            if complement in seen:
                return [seen[complement], index]

            seen[number] = index

        return []