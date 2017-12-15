# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/15 9:32
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
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies_types = len(set(candies))
        candies_number = len(candies) / 2
        return min(candies_types, candies_number)


if __name__ == "__main__":
    """
    Given an integer array with even length, where different numbers in this 
    array represent different kinds of candies. Each number means one candy 
    of the corresponding kind. You need to distribute these candies equally 
    in number to brother and sister. Return the maximum number of kinds of 
    candies the sister could gain.
    Example 1:
        Input: candies = [1,1,2,2,3,3]
        Output: 3
    Example 2:
        Input: candies = [1,1,2,3]
        Output: 2
    Note:
        The length of the given array is in range [2, 10,000], and will be 
        even.
        The number in given array is in range [-100,000, 100,000].
    """
    s = Solution()
    # candies = [1, 1, 2, 2, 3, 3]
    candies = [1, 1, 2, 3]
    output = s.distributeCandies(candies)
    print candies
    print output
