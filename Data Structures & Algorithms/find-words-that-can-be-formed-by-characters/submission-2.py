class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
       count=Counter(chars)
       res=0
       for w in words:
        if not Counter(w)-count:
            res+=len(w)
       return res