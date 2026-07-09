class Solution(object):
    def firstUniqChar(self, s):
        count = {}

        # Count frequency of each character
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Find the first character with frequency 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
        
        