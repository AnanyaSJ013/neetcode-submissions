class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = sorted(s)
        hash2 = sorted(t)
        if hash1==hash2:
            return True
        else:
            return False
