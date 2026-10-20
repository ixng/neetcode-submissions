class Solution:

    def encode(self, strs: List[str]) -> str:
         res = ""
         for s in strs:
            length_of_s = len(s)
            res += str(length_of_s)
            res +="£"
            res += s

         return res




    def decode(self, s: str) -> List[str]:
        res = []
        pos = 0
            
        while pos < len(s):
            num = ""
            word = ""
            while s[pos] != "£":
                num+=s[pos]
                pos+=1
            
            pos+=1
            num = int(num)

            for k in range(pos,pos + num):
                word+=s[k]

            res.append(word)
            pos+=num
        
        return res
            
             

            

            
             


        
        