class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # populate the hashmap with the order
        idx_mp = {}
        for i in range(len(order)):
            idx_mp[order[i]] = i
        # custom method to define the equality logic because of the custom order we're given
        def is_smaller(a,b):
            cl = min(len(a),len(b))
            for i in range(cl):
                # for example a="word" b = "world"
                # when we reach a-> d and b-> l we check if the order is correct 
                if a[i] != b[i]:
                    return idx_mp[a[i]] < idx_mp[b[i]]
            #what if nothing happened above ?
            # if a is smaller, return true for example a="he" b="hello"
            return len(a) < len(b)
        for i in range(1,len(words)):
            if words[i] != words[i-1] and (not is_smaller(words[i-1],words[i])):
                return False
        return True