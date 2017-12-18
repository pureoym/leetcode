# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/18 15:07
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
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s可以被分成：s.left，s.center，s.right三部分，其中s.left与
        # s.right是对称相等的，最大长度为len(s)/2，余下部分为s.center。
        # 如果s是可去单子回文，那么s.left和s.right必定对称相等，且
        # s.center是可去单子回文，其中可去单子位于s.center的首尾，而
        # s.center去掉首或尾的余下部分满足逆序相等：x=x[::-1]。
        # 如果s是回文，以上逻辑也满足。
        size = len(s)
        index = 0
        while index < size / 2 and s[index] == s[~index]:
            index += 1
        s = s[index:size - index]  # 将s变成s.center
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]


if __name__ == '__main__':
    """
    Given a non-empty string s, you may delete at most one character. Judge 
    whether you can make it a palindrome.
    Example 1:
        Input: "aba"
        Output: True
    Example 2:
        Input: "abca"
        Output: True
        Explanation: You could delete the character 'c'.
    Note:
        The string will only contain lowercase characters a-z. The maximum 
        length of the string is 50000.
    """
    s = Solution()
    input_str = "abca"
    output = s.validPalindrome(input_str)
    print input_str
    print output
