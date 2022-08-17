# Time Complexity : O(n^3)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#
#
# Your code here along with comments explaining your approach

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        m = len(nums)
        dp = []
        for i in range(m):
            dp.append([0] * m)
        for l in range(1, m + 1):
            for i in range(m - l + 1):
                j = i + l - 1
                maxi = 0
                for k in range(i, j + 1):
                    left = 1
                    right = 1
                    if i != 0:
                        left = nums[i - 1]
                    if j != m - 1:
                        right = nums[j + 1]
                    curr = left * nums[k] * right
                    before = 0
                    after = 0
                    if k != i:
                        before = dp[i][k - 1]
                    if k != j:
                        after = dp[k + 1][j]
                    maxi = max(maxi, before + curr + after)
                dp[i][j] = maxi
        return dp[0][m - 1]


print(Solution().maxCoins([3, 1, 5, 8]))
