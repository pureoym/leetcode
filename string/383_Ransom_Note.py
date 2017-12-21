# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/21 15:41
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
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_list = "abcdefghijklmnopqrstuvwxyz"
        for char in char_list:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True


if __name__ == "__main__":
    """
    Given an arbitrary ransom note string and another string containing letters from
    all the magazines, write a function that will return true if the ransom note can
    be constructed from the magazines ; otherwise, it will return false. Each letter 
    in the magazine string can only be used once in your ransom note.
    Note:You may assume that both strings contain only lowercase letters.
    用magazine中的字母拼ransomNote字符串，magazine中每个字母只能用一次。返回是否可拼。
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
    """
    s = Solution()
    a = "aa"
    b = "aab"
    output = s.canConstruct(a, b)
    print "canConstruct(\"%s\",\"%s\") -> %s" % (a, b, output)
