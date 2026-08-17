class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            n = len(s)
            res += str(n) + "#" + s
        
        return res 

    def decode(self, s: str) -> List[str]:
        res_arr = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#": 
                j +=1 
            length = int(s[i:j]) 
            res_arr.append(s[j+1 : j+length+1])
            i = j+length+1
        return res_arr
            
            
