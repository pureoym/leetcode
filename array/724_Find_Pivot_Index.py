# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/15 14:02
# Copyright 2017 pureoym. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time:O(n)
        # Space:O(1)
        left, right = 0, sum(nums)
        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
        return -1


if __name__ == '__main__':
    """
    注意时间复杂度
    Example 1:
        Input: 
        nums = [1, 7, 3, 6, 5, 6]
        Output: 3
        Explanation: 
        The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the 
        sum of numbers to the right of index 3.Also, 3 is the first index where this
        occurs.
    Example 2:
        Input: 
        nums = [1, 2, 3]
        Output: -1
        Explanation: 
        There is no index that satisfies the conditions in the problem statement.
    Note:
        The length of nums will be in the range [0, 10000].
        Each element nums[i] will be an integer in the range [-1000, 1000].
    """
    s = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    output = s.pivotIndex(nums)
    print nums
    print output
