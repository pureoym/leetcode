# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/21 16:48
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
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # at_least:最少出现的(的个数，至少需要)的个数
        # at_most:最多可能出现的(的个数，至多需要)的个数
        # 需要满足：
        # 1：at_most 永远非负
        # 2：at_least 循环结束后为零
        at_least = at_most = 0

        for char in s:
            if char == "(":
                at_least += 1  # +1
                at_most += 1  # +1
            if char == ")":
                at_least = max(at_least - 1, 0)  # -1/-0
                at_most -= 1  # -1
            if char == "*":
                # 可以是 ( * ) 中的任何一个
                at_least = max(at_least - 1, 0)  # -1/-0
                at_most += 1  # +1
            if at_most < 0:
                return False

        return at_least == 0


if __name__ == "__main__":
    """
    Given a string containing only three types of characters: '(', ')' and '*', 
    write a function to check whether this string is valid. We define the validity 
    of a string by these rules:
        1,Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        2,Any right parenthesis ')' must have a corresponding left parenthesis '('.
        3,Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        4,'*' could be treated as a single right parenthesis ')' or a single left 
        parenthesis '(' or an empty string.
        5,An empty string is also valid.
    Examples:
        Input: "()" Output: True
        Input: "(*)" Output: True
        Input: "(*))" Output: True
        Input: "(*()" Output: True
    Note:
        The string size will be in the range [1, 100].
    """
    s = Solution()
    input_str = "(*)"
    output = s.checkValidString(input_str)
    print input_str
    print output
