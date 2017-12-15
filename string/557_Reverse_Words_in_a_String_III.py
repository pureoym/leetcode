# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/14 16:25
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
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # output_str = ''
        # for one in s.split():
        #     output_str += one[::-1] + ' '
        # return output_str.strip()
        return " ".join(map(lambda x: x[::-1], s.split()))


if __name__ == '__main__':
    """
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    """

    s = Solution()
    input_str = "Let's take LeetCode contest"
    output_str = s.reverseWords(input_str)
    print input_str
    print output_str