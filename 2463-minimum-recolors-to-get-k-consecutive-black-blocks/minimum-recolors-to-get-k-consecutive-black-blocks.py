class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wc = 0
        n = len(blocks)
        l = []
        
        # Count 'W' in the first window of size k
        for i in range(k):
            if blocks[i] == 'W':
                wc += 1
        l.append(wc)
        
        # Slide the window across the string
        for i in range(k, n):
            if blocks[i - k] == 'W':  # Remove leftmost character from window
                wc -= 1
            if blocks[i] == 'W':  # Add new rightmost character to window
                wc += 1
            l.append(wc)

        return min(l)
