import pandas as pd


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
    
def check():
    for t in range(df.shape[0]):
        if not int(to_int.romanToInt(df.iloc[t,1])) == int(df.iloc[t,0]):
            print(int(df.iloc[t,0]))
            return False
    return True

to_int = Solution()

df = pd.read_excel('test.xlsx', header = None)

assert (check() == True), 'Функция должна работать на всех числах от 1 до 3999'
