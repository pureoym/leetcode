# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/21 10:05
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
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        period = 1
        length = len(s)
        while period < length:
            if length % period == 0:
                n = length / period
                if s[:period] * n == s:
                    return True
            period += 1
        return False


if __name__ == "__main__":
    """
    Given a non-empty string check if it can be constructed by taking a substring of 
    it and appending multiple copies of the substring together. You may assume the 
    given string consists of lowercase English letters only and its length will not 
    exceed 10000.
    判断字符串序列是否可以被其子序列周期性的拼接而成。
    Example 1:
        Input: "abab"
        Output: True
        Explanation: It's the substring "ab" twice.
    Example 2:
        Input: "aba"
        Output: False
    Example 3:
        Input: "abcabcabcabc"
        Output: True
        Explanation: It's the substring "abc" four times. And the substring "abcabc" 
        twice.
    """
    s = Solution()
    input_str = "abcabcabcabc"
    output = s.repeatedSubstringPattern(input_str)
    print input_str
    print output
