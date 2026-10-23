class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_to_open = { ")" : "(", "]" : "[", "}" : "{"}

        for ch in s:
            if ch in closed_to_open and stack:
                if stack[-1] == closed_to_open[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        if not stack:
            return True 
        return False 