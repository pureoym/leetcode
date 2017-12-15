# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/15 16:37
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
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        result = True
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                result = False
            else:
                i += 1
                result = True
        return result


if __name__ == '__main__':
    """
    We have two special characters. The first character can be represented by one bit 0. 
    The second character can be represented by two bits (10 or 11).Now given a string 
    represented by several bits. Return whether the last character must be a one-bit 
    character or not. The given string will always end with a zero.
    Example 1:
        Input: bits = [1, 0, 0]
        Output: True
        Explanation: The only way to decode it is two-bit character and one-bit character. 
        So the last character is one-bit character.
    Example 2:
        Input: bits = [1, 1, 1, 0]
        Output: False
        Explanation: The only way to decode it is two-bit character and two-bit character. 
        So the last character is NOT one-bit character.
    Note:
        1 <= len(bits) <= 1000.
        bits[i] is always 0 or 1.
    """
    s = Solution()
    bits = [1, 0, 0]
    output = s.isOneBitCharacter(bits)
    print bits
    print output
