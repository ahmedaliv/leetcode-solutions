class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        h_m = collections.defaultdict(int)

        for cp in cpdomains:
            count,sds = cp.split(" ")
            sds = sds.split(".")
            tp = sds[-1]
            h_m[tp] += int(count)
            for i in range(len(sds)-2,-1,-1):
                cur_domain = f'{sds[i]}.{tp}'
                h_m[cur_domain] += int(count)
                tp  = f'{sds[i]}.{tp}'
        return [f"{v} {k}" for k,v in h_m.items()]