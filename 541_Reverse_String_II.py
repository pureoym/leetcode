# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/15 8:55
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
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        index = 0
        while index < len(s):
            if index % (2 * k) == 0:
                result += s[index:index + k][::-1]
            else:
                result += s[index:index + k]
            index += k
        return result


if __name__ == '__main__':
    """
    Given a string and an integer k, you need to reverse the first k characters 
    for every 2k characters counting from the start of the string. If there are 
    less than k characters left, reverse all of them. If there are less than 2k 
    but greater than or equal to k characters, then reverse the first k characters 
    and left the other as original.
    Example:
        Input: s = "abcdefg", k = 2
        Output: "bacdfeg"
    Restrictions:
        The string consists of lower English letters only.
        Length of the given string and k will in the range [1, 10000]
    """
    s = Solution()
    input_str = "abcdefg"
    k = 2
    output_str = s.reverseStr(input_str, k)
    print input_str
    print output_str
