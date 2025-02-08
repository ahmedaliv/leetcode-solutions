class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it))-ord('a')].append(it)
        
        ans = 0
        for c in s:
            c_idx = ord(c)-ord('a')
            old_list = heads[c_idx]
            heads[c_idx] = []
            while old_list:
                it = old_list.pop()
                nxt_char = next(it,None)
                if nxt_char:
                    heads[ord(nxt_char)-ord('a')].append(it)
                else:
                    ans+=1
        return ans