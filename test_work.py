class Solution:
     def romanToInt(self, s: str) -> int:
         # create main dictionary
        d = {'I':1 ,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000 }
    
        otv = 0  # for calculate solution
        it = 0   # for check every letter/number
    
        for i in range(len(s)):
    
            if it == len(s)-1:
                otv += d[s[it]]
                break
    
            if d[s[it]] < d[s[it+1]]:
                otv += d[s[it+1]] - d[s[it]]
                it += 2
            else:
                otv += d[s[it]]
                it +=1
            if it >= len(s):
                break
            
        return otv

to_int = Solution()
print(to_int.romanToInt('XII'))