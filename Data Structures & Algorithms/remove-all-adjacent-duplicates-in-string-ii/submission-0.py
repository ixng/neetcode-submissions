class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        if not s:
            return ""
        else:
            stack = []

        res = ""

        for ch in s:

            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop(-1)
            else:
                stack.append([ch,1]) 
            
        for char_tup in stack:
            for count in range(char_tup[1]):
                res+=(char_tup[0])
        
        return res