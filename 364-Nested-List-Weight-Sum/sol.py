def dfs(e, depth):
    if not isinstance(e, list):
        return e * depth
    return sum(dfs(x, depth + 1) for x in e)

def nested_weight_sum(nested_list):
    return sum(dfs(x, 1) for x in nested_list)


# BFS
from collections import deque
def nested_weight_sum(nested_list):

  queue = deque([(e,1) for e in nested_list])
  total = 0 
  while queue:
    e,depth = queue.popleft()
    if isinstance(e,list):
      queue.extend((x,depth+1) for x in e)
    else:
      total +=  e * depth
  return total
