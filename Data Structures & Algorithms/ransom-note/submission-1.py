class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        countA = {}
        countB = {}
        for ch in ransomNote:
            countA[ch] = 1 + countA.get(ch,0)

        for ch in magazine:
                countB[ch] = 1 + countB.get(ch,0)

        
        for ch in countA:
            if countB.get(ch,-1) < countA[ch]:
                return False
            
        return True 