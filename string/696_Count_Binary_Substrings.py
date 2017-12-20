# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/20 17:47
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
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

if __name__ == "__main__":
    """
    Give a string s, count the number of non-empty (contiguous) substrings that have
    the same number of 0's and 1's, and all the 0's and all the 1's in these substrings 
    are grouped consecutively. 
    Substrings that occur multiple times are counted the number of times they occur.
    计算出输入序列的满足条件的子序列数量，条件：
        1：该子序列的0的个数与1的个数相同；
        2：该子序列中所有的0位于一侧，所有的1位于另一侧。
    元素相同的子序列出现多次，则计数多次。
    输入序列长度为1至50000，仅包含字符0与字符1。
    Example 1:
        Input: "00110011"
        Output: 6
        Explanation: There are 6 substrings that have equal number of consecutive 1's 
        and 0's: "0011", "01", "1100", "10", "0011", and "01".Notice that some of these
        substrings repeat and are counted the number of times they occur.Also, "00110011"
        is not a valid substring because all the 0's (and 1's)are not grouped together.
    Example 2:
        Input: "10101"
        Output: 4
        Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number
        of consecutive 1's and 0's.
    Note:
        s.length will be between 1 and 50,000.
        s will only consist of "0" or "1" characters.
    """
    s = Solution()
    input_str = "00110011"
    output_str = s.countBinarySubstrings(input_str)
    print input_str
    print output_str
