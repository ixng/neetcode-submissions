class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        if not s:
            return ""
        
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()    
            else:
                stack.append([ch,1])    
            
            # [["a", 2]]
        return "".join(ch * count for ch, count in stack)