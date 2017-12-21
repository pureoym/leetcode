# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/21 14:41
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
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ban_dict = []
        # for i in range(len(s)):
        #     if s[i] in ban_dict:
        #         continue
        #     elif s[i] in s[i + 1:]:
        #         ban_dict.append(s[i])
        #     else:
        #         return i
        # return -1
        char_list = "abcdefghijklmnopqrstuvwxyz"
        single_char_index = []
        for char in char_list:
            if s.count(char) == 1:
                single_char_index.append(s.find(char))
        return min(single_char_index) if len(single_char_index) > 0 else -1


if __name__ == "__main__":
    """
    Given a string, find the first non-repeating character in it and return
    it's index. If it doesn't exist, return -1.
    寻找字符串中第一次仅出现过一次的字符的下标，没有返回-1.
    Examples:
        s = "leetcode", return 0.
        s = "loveleetcode", return 2.
    Note: You may assume the string contain only lowercase letters.
    """
    s = Solution()
    input_str = "loveleetcode"
    output = s.firstUniqChar(input_str)
    print input_str
    print output
