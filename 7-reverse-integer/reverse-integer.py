class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0
        limit = 2147483648 if sign == -1 else 2147483647

        while x > 0:
            digit = x % 10
            x //= 10

            if result > (limit - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result