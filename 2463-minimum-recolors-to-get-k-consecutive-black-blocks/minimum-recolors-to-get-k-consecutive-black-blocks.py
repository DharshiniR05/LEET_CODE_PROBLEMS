class Solution(object):
    def minimumRecolors(self, blocks, k):
        white = blocks[:k].count('W')
        min_operations = white

        # Slide the window
        for i in range(k, len(blocks)):
            # Remove left character
            if blocks[i - k] == 'W':
                white -= 1

            # Add new right character
            if blocks[i] == 'W':
                white += 1

            min_operations = min(min_operations, white)

        return min_operations
        