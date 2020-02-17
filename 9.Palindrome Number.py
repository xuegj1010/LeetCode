"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = x
        if x < 0:
            return False
        elif 0 <= x < 10:
            return True
        else:
            l = []
            while x // 10 > 0:
                y = x % 10
                x = x // 10
                l.append(y)
                if x < 10:
                    l.append(x)
            a = len(l)
            sum = 0
            for i in l:
                sum += i * 10 ** (a - 1)
                a -= 1
            if c == sum:
                return True
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1))
