class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        def is_smaller(a,b):
            l = min(len(a),len(b))
            for i in range(l):
                if a[i] != b[i]:
                    return mp[a[i]] < mp[b[i]]
            return len(a) < len(b)
        for i in range(len(order)):
            mp[order[i]] = i
        
        for i in range(1,len(words)):
            if words[i]!=words[i-1] and not(is_smaller(words[i-1],words[i])):
                return False
        return True