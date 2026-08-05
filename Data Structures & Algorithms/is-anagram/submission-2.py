class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        x = {}
        y = {}

        sorted(s)
        sorted(t)
        for l in s:
            if l in x:
                x[l] += 1
            else:
                x[l] = 1

        for l in t:
            if l in y:
                y[l] += 1
            else:
                y[l] = 1

        for p in x:
            if x[p] != y.get(p,0):
                return False

        return True 


