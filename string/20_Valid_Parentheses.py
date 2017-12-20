# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/20 15:29
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
    def isValid(self, s):
        """
        使用栈stack这种储存方式。stack=[]
        设：A="(",a=")",B="[",b="]",C="{",c="}"。
        其中，当Aa连续相遇时出栈，Bb连续相遇时出栈，Cc连续相遇时出栈。
        对于输入：s="[()][]}"，stack的变化过程为：
            step 0: stack=[C]
            step 1: stack=[CB]
            step 2: stack=[CBA]
            step 3: stack=[CBAa]=[CB]
            step 4: stack=[CBb]=[C]
            step 5: stack=[CB]
            step 6: stack=[CBb]=[C]
            step 7: stack=[Cc]=[]
            当stack为空时，符合条件，返回True。
        对于输入：s="[()"
            step 0: stack=[B]
            step 1: stack=[CA]
            step 2: stack=[CAa]=[C]
            当stack非空时，不符合条件，返回False。
        对于输入：s="[(])"
            step 0: stack=[B]
            step 1: stack=[CA]
            step 2: stack=[CAb]
            当出现Ab这种不成对现象时，不符合条件，提前返回False。
        :type s: str
        :rtype: bool
        """
        # stack = []
        # left = ["(", "[", "{"]
        # right = [")", "]", "}"]
        # for char in s:
        #     if char in left:
        #         stack.append(char)
        #     else:
        #         if len(stack) == 0:
        #             return False
        #         elif stack[-1] != left[right.index(char)]:
        #             return False
        #         else:
        #             stack.pop()
        # return len(stack) == 0
        stack = []
        dict = {")": "(", "]": "[", "}": "{"}
        left = ["(", "[", "{"]
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] != dict.get(char):
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.The brackets must close in the correct 
    order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
    """
    s = Solution()
    input_str = "()"
    output_str = s.isValid(input_str)
    print input_str
    print output_str
