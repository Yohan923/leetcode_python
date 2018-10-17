"""Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2."""

class Solution:

    """two pointers at two ends, since area is limited by the width of the box created. each time
    pointer of the shorter line is moved towards the longer line as the area is limited by the shorter line
    until pointers hit each other. return the highest area from the loop"""
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        max_area = 0

        while i < j:
            max_area = max(max_area, (min(height[i], height[j]) * (j-i)))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

