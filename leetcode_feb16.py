class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        if len(nums) < 2:
            return res

        mappings = {}
        for i in xrange(len(nums)):
            if target - nums[i] in mappings:
                res.append(mappings.get(target - nums[i]))
                res.append(i + 1)
                break
            mappings[nums[i]] = i + 1
        return res

    # container with most water
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        res = 0
        if len(height) < 2:
            return res

        i, j = 0, len(height) - 1

        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # need to remove duplicate in result set
        res = []
        if len(nums) < 3:
            return res
        #numsorted = sorted(nums)
        nums.sort()

        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return res


s = Solution()
nums = [14,9,14,-9,-6,-10,2,6,-11,-5,12,-6,6,-6,-9,-1,-14,7,-9,13,8,9,9,10,8,5,-10,-11,-9,-4,-15,-10,-10,-15,-12,-9,12,5,4,-14,-15,1,-5,-2,3,-7,4,4,-14,10,2,1,-4,-12,-12,-11,8,-7,-15,6,4,8,11,1,0,6,-1,-3,-12,-12,-10,10,4,-8,-15,14,0,5,3,1,-8,-9,9,4,-14,12,8,10,12,1,1,-7,-6,-10,1,9,3,-15,13,7,-12,-12,-6,0]
res = s.threeSum(nums)
print res
