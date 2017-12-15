# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/15 14:59
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
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 需要构造数据，元素个数为m+n
        # 从最大元素nums1[m+n-1]开始赋值，从num1或num2中的最后一位中挑选大者
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if m == 0:
            nums1[:n] = nums2[:n]


if __name__ == '__main__':
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one 
    sorted array.
    Note:
        You may assume that nums1 has enough space (size that is greater or equal 
        to m + n) to hold additional elements from nums2. The number of elements 
        initialized in nums1 and nums2 are m and n respectively. 
    """
    s = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print nums1
