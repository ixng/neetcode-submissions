class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        an = list()
        for st in strs:
            charac = [0] * 26

            for cha in st:
                charac[ord(cha) - ord('a')] +=1
        
            ans[tuple(charac)].append(st)

        for lis in ans:
            an.append(ans[lis])

        return an