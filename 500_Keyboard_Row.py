# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/14 17:00
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
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = set('zxcvbnm')
        r2 = set('asdfghjkl')
        r3 = set('qwertyuiop')
        result = []
        for word in words:
            w = set(word.lower())
            if w.issubset(r1) or w.issubset(r2) or w.issubset(r3):
                result.append(word)
        return result


if __name__ == '__main__':
    """
    返回符合条件的单词列表，条件为：可以用键盘的一行中的按键打出
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]
    """
    s = Solution()
    input_words = ["Hello", "Alaska", "Dad", "Peace"]
    output_words = s.findWords(input_words)
    print input_words
    print output_words
