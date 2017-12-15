# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/14 10:14
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
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        z_str = bin(z).replace('0b', '')
        result = z_str.count('1')
        return result


if __name__ == "__main__":
    """
    input: two bin
    output: hamming distance of input
    """
    s = Solution()
    x = 0b0011000011110000111100001111000011110000111100001111000011110000
    y = 0b1111000011110000111100001111000011110000111100001111000011111111
    print s.hammingDistance(x, y)
    import time

    t1 = time.time()
    for i in range(100000):
        s.hammingDistance(x, y + i)
    t2 = time.time()
    print t2 - t1
