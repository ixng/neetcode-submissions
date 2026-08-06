class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs: 
            cha = [0] * 26

            for ch in string:
                cha[ord(ch) - ord("a")] +=1

            res[tuple(cha)].append(string)
        return list(res.values())


            


        

        
        
