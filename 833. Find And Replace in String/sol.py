class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replace_map = {}

        for i in range(len(indices)):
            idx = indices[i]
            src = sources[i]
            tar = targets[i]
            if s.startswith(src,idx):
                replace_map[idx] = (src,tar)
            
        i = 0 
        result = []
        while i < len(s):
            if i in replace_map:
                src,tar = replace_map[i]
                result.append(tar)
                i += len(src)
            else:
                result += s[i]
                i += 1
        return ''.join(result)
