class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for i in range(0,len(s)):
            if s[i].isalnum():
                str = str+s[i]

        str = str.lower()
        return str==str[::-1]
