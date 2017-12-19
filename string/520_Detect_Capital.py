# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/19 9:12
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
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower():
            return True
        if word.isupper():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False


if __name__ == "__main__":
    """
    Given a word, you need to judge whether the usage of capitals in it is 
    right or not.We define the usage of capitals in a word to be right when
    one of the following cases holds:
        1.All letters in this word are capitals, like "USA".
        2.All letters in this word are not capitals, like "leetcode".
        3.Only the first letter in this word is capital if it has more 
        than one letter, like "Google".
    Otherwise, we define that this word doesn't use capitals in a right way.
    Example 1:
        Input: "USA"
        Output: True
    Example 2:
        Input: "FlaG"
        Output: False
    Note: The input will be a non-empty word consisting of uppercase and 
        lowercase latin letters.
    """
    s = Solution()
    input_str = "TesT"
    output = s.detectCapitalUse(input_str)
    print input_str
    print output
