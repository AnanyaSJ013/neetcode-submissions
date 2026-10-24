class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d={start for start, end in paths}
        for start, end in paths:
            if end not in d:
                return end
        return ""
