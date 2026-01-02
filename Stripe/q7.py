#braces expression II


class Solution:
    def braceExpansionII(self, s: str) -> List[str]:
        def getWord():
            nonlocal i
            word = ""
            while i < len(s) and s[i].isalpha():
                word += s[i]
                i += 1
            return word
        
        
        def dfs():
            nonlocal i
            res = set()
            if s[i] == '{':
                i += 1
                res.update(dfs())
                while i < len(s) and s[i] == ',':
                    i += 1
                    res.update(dfs())
                i += 1
            elif s[i].isalpha():
                res.add(getWord())

            while i < len(s) and (s[i] == '{' or s[i].isalpha()): 
                res = {w + a for a in dfs() for w in res}
            return res

        i = 0
        return sorted(dfs())