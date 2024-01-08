from typing import List

class Solution:
    def SelectionSort(self,nums):

        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min_idx]:
                    min_idx = j

            nums[i], nums[min_idx] =  nums[min_idx],nums[i]
        return nums



nums = [64,25,12,22,11]
p = Solution()
nums = p.SelectionSort(nums)

for i in range(len(nums)):
    print(nums[i])

