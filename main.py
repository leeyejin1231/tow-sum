from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    dp = {}

    for i, num in enumerate(nums):
        remain = target - num

        if remain not in dp:
            dp[num] = i
        else:
            return[dp[remain], i]

    return []

# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 2, 4], 6))
# print(twoSum([3, 3], 6))