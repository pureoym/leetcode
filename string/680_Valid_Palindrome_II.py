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
        return False


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
    """
    s = Solution()
    input_str = "abca"
    output = s.validPalindrome(input_str)
    print input_str
    print output
