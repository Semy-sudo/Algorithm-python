class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lis1 = []
        lis2 = []
        for char in s:
            if char not in lis1:
                lis1.append(char)
            else:
                lis2.append(char)
        
        ans = []
        for char in lis1:
            if char not in lis2:
                ans.append(char)
                
        ans += lis2
        
        return "".join(ans)
            
        