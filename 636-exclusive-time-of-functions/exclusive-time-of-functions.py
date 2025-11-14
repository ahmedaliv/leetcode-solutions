class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0]*n
        for log in logs:
            fn_id,typ,ts = log.split(":")
            fn_id = int(fn_id)
            ts = int(ts)
            if typ == "start":
                if stack:
                    res[stack[-1][0]] += ts- stack[-1][1]
                stack.append([fn_id,ts])
            else:
                start_id,start_time = stack.pop()
                res[start_id] += ts - start_time + 1
                if stack:
                    stack[-1][1] = ts +1
        return res
