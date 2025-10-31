class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.canonical(s) == self.canonical(t)

    def canonical(self,s):
        index_mapping = {}
        can_str = []
        for i,c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            can_str.append(str(index_mapping[c]))
        return ' '.join(can_str)