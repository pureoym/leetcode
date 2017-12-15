# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/15 9:59
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
import numpy as np


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        column = len(nums[0])
        if r * c != row * column:
            return nums
        else:
            return np.reshape(nums, (r, c)).tolist()


if __name__ == '__main__':
    """
    Example 1:
        Input: nums = [[1,2],[3,4]], r = 1, c = 4
        Output: [[1,2,3,4]]
    Explanation:
        The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 
        1 * 4 matrix, fill it row by row by using the previous list.
   Example 2:
        Input: nums = [[1,2],[3,4]],r = 2, c = 4
        Output:[[1,2],[3,4]]
    Explanation:
        There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output 
        the original matrix.     
    """
    s = Solution()
    nums = [[1, 2], [3, 4]]
    output = s.matrixReshape(nums, 1, 4)
    print nums
    print output
