# -*- coding: utf-8 -*-
# author: pureoym
# time: 2017/12/15 11:15
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
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                # if grid[i][j] == 1:
                #     if i == 0:
                #         perimeter += 1
                #     if i == width - 1:
                #         perimeter += 1
                #     if j == 0:
                #         perimeter += 1
                #     if j == height - 1:
                #         perimeter += 1
                #     if i - 1 >= 0 and grid[i - 1][j] == 0:
                #         perimeter += 1
                #     if i + 1 < width and grid[i + 1][j] == 0:
                #         perimeter += 1
                #     if j - 1 >= 0 and grid[i][j - 1] == 0:
                #         perimeter += 1
                #     if j + 1 < height and grid[i][j + 1] == 0:
                #         perimeter += 1
                if grid[i][j] == 1:
                    perimeter += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter


if __name__ == '__main__':
    """
    Example:
        一个矩阵组成的地图。1代表陆地，0代表水域。求周长。
        [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
        Answer: 16
    """
    s = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    # grid = [[1]]
    # grid = [[0, 0, 1, 1], [1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
    perimeter = s.islandPerimeter(grid)
    print grid
    print perimeter
