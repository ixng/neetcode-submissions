class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(i,j):
            while i < j:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            
        
        i = 0 
        s = list(s)
        while i < len(s):
            if s[i] != ' ':
                j = i
                while j < len(s) and s[j] != ' ': #checks if its there is more of the word and then if the str has not ended it will check if there it is on a space before adding to the word 
                    j+=1
                reverse(i,j-1)
                i = j + 1


        return ''.join(s)
