class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(indices)
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        
        res = []
        i = 0
        ptr = 0 
        
        while i < len(s):
            replaced = False
            for idx, src, tgt in replacements:
                if i == idx and s[i:i+len(src)] == src:
                    res.append(tgt)
                    i += len(src)
                    replaced = True
                    break 
            if not replaced:
                res.append(s[i])
                i += 1
        return ''.join(res)