class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        ab = []
        for st in strs:
            sortedStr = ''.join(sorted(st))
            ans[sortedStr].append(st)

        for lis in ans:
            ab.append(ans[lis])

        return ab