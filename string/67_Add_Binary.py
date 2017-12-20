# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/20 8:52
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
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = int(a, 2)
        b1 = int(b, 2)
        return bin(a1 + b1)[2:]


if __name__ == "__main__":
    """
    Given two binary strings, return their sum (also a binary string).
    For example,
        a = "11"
        b = "1"
        Return "100".
    """
    s = Solution()
    a = "11"
    b = "1"
    output_str = s.addBinary(a, b)
    print a, b
    print output_str
