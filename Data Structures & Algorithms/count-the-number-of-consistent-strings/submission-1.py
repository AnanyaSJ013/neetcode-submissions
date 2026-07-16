class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        res=len(words)
        for w in words:
           for c in w:
            if c not in a:
                res-=1
                break
        return res