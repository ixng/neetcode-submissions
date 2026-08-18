class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        
        
        res = ''.join(filter(str.isalnum,s))
        
        r = len(res) - 1
        while l < r:
            if res[l] == ' ' :
                l+=1
            
            if res[r] == ' ':
                r-=1 

            if res[l].lower() == res[r].lower():
                r-=1
                l+=1
            else:
                return False
        
        return True
            
