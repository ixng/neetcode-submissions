class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {"}" : "{", "]" : "[", ")" : "("}
        stack = [] 

        for ch in s:
            if ch in closed_to_open and stack:
                if closed_to_open[ch] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(ch)

        if not stack:
            return True

        return False
        