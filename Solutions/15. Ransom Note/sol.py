class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = collections.defaultdict(int)
        for c in magazine:
            m[c]+=1
        for c in ransomNote:
            if not m[c]:
                return False
            m[c]-=1
        return True