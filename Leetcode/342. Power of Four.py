"""
342. Power of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
Input: 16
Output: true

Example 2:
Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""
# Time complexity: O(1)
# Space complexity: O(1)
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1
