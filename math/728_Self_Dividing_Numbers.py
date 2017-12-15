# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/14 10:31
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
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # if not (1 <= left <= right <= 10000):
        #     return []
        # result = filter(is_self_dividing, range(left, right + 1))
        # return result
        is_self_dividing = lambda num: \
            '0' not in str(num) and \
            all(num % int(digit) == 0 for digit in str(num))
        return filter(is_self_dividing, range(1, (right + 1)))


# def is_self_dividing(number):
#     n = number
#     while n > 0:
#         i = n % 10
#         if i == 0:
#             return False
#         else:
#             if number % i != 0:
#                 return False
#         n = n / 10
#     return True


if __name__ == '__main__':
    """
    input:输入从left到right的数列
    output:该数列中符合条件的数组成的数列。条件为：该数能被自身的每一位整除
    """
    s = Solution()
    print s.selfDividingNumbers(1, 22)
