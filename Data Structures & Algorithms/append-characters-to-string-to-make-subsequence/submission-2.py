class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp = 0
        tp = 0
        
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
                continue
            
            while sp < len(s) and s[sp] != t[tp]:
                sp += 1
        
        return len(t) - tp
