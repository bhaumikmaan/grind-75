class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0]*128
        for c in s:
            freq[ord(c)] += 1
        odd = 0
        for i in freq: odd += i & 1
        return len(s) - odd + (odd > 0) 