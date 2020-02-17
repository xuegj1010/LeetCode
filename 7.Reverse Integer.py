"""
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reversed_x = int(str(x)[::-1])
        else:
            reversed_x = - int(str(x)[:0:-1])
        if -2 ** 31 < reversed_x < 2 ** 31 - 1:
            return reversed_x
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
