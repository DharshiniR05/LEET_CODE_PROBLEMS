class Solution(object):
    def isSameAfterReversals(self, num):
        rev1 = int(str(num)[::-1])
        rev2 = int(str(rev1)[::-1])

        return rev2 == num
        