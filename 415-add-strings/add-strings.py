class Solution(object):
    def addStrings(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += ord(num1[i]) - ord('0')
                i -= 1

            if j >= 0:
                total += ord(num2[j]) - ord('0')
                j -= 1

            result = str(total % 10) + result
            carry = total // 10

        return result
        