class Solution(object):
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Count vowels in first window
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            # Remove left character
            if s[i - k] in vowels:
                count -= 1

            # Add new character
            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count
        