from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
      mp = defaultdict(list)
      # for s in strings:
      #   # how many chars are we from 'a'
      #   diff = ord(s[0]) - ord('a')
      #   t = []
      #   for c in s:
      #     # we shift each char by that diff(from a), so we finally get a canonical form for each string
      #     shifted = (ord(c) - ord('a') - diff) % 26
      #     # we convert it again to a character
      #     t.append(chr(shifted+ord('a')))
      #   key = ''.join(t)
      #   mp[key].append(s)
      # return list(mp.values())
      for s in strings:
          key = tuple(ord(c) - ord(s[0]) for c in s)
          mp[key].append(s)
      return list(mp.values())
