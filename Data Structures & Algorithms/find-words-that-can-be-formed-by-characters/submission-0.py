class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
       count=Counter(chars)
       res=0
       for w in words:
        cur=Counter(w)
        good=True
        for c in cur:
            if cur[c]>count[c]:
                good=False
                break
        if good:
            res+=len(w)
       return res