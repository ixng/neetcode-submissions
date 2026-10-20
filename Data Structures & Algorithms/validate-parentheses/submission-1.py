class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = { "]" : "[", "}" : "{", ")" : "("}
        stack = []

        for char in s:
            #checks if its a closed bracket and if it is then check whether the last element in stack is the opening of the bracket and if true then pop the opening. 
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack == []:
            return True

        return False 
                    
        
        


