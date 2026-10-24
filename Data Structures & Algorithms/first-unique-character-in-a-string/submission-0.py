class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        

        count = Counter(s)

        for c in count:
            if count[c] == 1:
                return s.index(c)
        
        return -1 