class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0
        n = len(chars)

        while i < len(chars):
            chars[k] = chars[i]
            k += 1
            j = i + 1
            
            while j < n and chars[i] == chars[j]:
                j += 1
            
            if j - i > 1:
                count = j - i
                digits = list(str(count))
                for d in digits:
                    chars[k] = d
                    k += 1
            i = j
        
        return k