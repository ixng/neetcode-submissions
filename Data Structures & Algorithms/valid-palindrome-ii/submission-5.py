class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        removal = False
        def isPalindrome(l,r):
            while l<r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True 
        while l<r:
            if s[r] != s[l]:
                return isPalindrome(l+1,r) or isPalindrome(l,r-1)
            l+=1
            r-=1
        return True 