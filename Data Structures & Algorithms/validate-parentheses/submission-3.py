class Solution:
    def isValid(self, s: str) -> bool:
        #stack is used to track the opening brackets so then when we find a closing bracket we can check that the last bracket pushed matches the closing bracket and then just pop it because it is not used anymore and now move onto the next open bracket before it.
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
        
        return True if not stack else False 
                    
        
        


