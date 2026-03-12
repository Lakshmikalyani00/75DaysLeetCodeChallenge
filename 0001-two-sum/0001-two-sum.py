class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in lookup:
                return [lookup[diff], index]

            lookup[value] = index