class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        s = []
        res = [0]*n
        def parse(s):
            l = s.split(":")
            l[0]  = int(l[0])
            l[2] = int(l[2])
            return l

        for log in logs:
            id,tp,t = parse(log)
            if tp == "start":
                if s:
                    par = s.pop()
                    res[par[0]]+=t - par[2] 
                    par[2] = t
                    s.append(par)
                s.append(parse(log))
            else:
                tp = s.pop()
                total=t-tp[2]+1
                res[tp[0]] += total

                if s:
                    tp = s.pop()
                    tp[2] = t +1
                    s.append(tp)
        return res
                