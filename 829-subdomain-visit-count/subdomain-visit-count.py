class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def my_split(s, sep=None):
            result, word = [], ""
            for char in s:
                if char == sep or (sep is None and char.isspace()):
                    if word or sep is not None:
                        result.append(word)
                    word = ""
                else:
                    word += char
            if word:
                result.append(word)
            return result
        h_m = collections.defaultdict(int)

        for cp in cpdomains:
            count,sds = my_split(cp," ")
            sds = my_split(sds,".")
            tp = sds[-1]
            h_m[tp] += int(count)
            for i in range(len(sds)-2,-1,-1):
                cur_domain = f'{sds[i]}.{tp}'
                h_m[cur_domain] += int(count)
                tp  = f'{sds[i]}.{tp}'
        return [f"{v} {k}" for k,v in h_m.items()]
