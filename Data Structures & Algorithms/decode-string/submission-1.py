class Solution:
    def decodeString(self, s: str) -> str:
        

        if not s:
            return ""

        numStack , strStack = [] , []
        currNum , currStr = "", ""

        for ch in s:
            if ch.isdigit():
                currNum+=ch
            elif ch.isalpha():
                currStr+=ch
            elif ch == "[":
                
                numStack.append(int(currNum))
                strStack.append(currStr)
                currNum = "" 
                currStr = ""
            else: # if ch == "]"
                currStr = strStack.pop() + numStack.pop() * currStr
        
        return currStr
