class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c=defaultdict(int)
        for w in words:
            for i in w:
                c[i]+=1
        for i in c:
            if c[i]%len(words):
                return False
        return True