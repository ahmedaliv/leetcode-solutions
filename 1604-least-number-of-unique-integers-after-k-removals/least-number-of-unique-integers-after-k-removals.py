from collections import Counter
from sortedcontainers import SortedDict

class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        freq_count = SortedDict()

        for num, count in freq.items():
            if count in freq_count:
                freq_count[count] += 1
            else:
                freq_count[count] = 1

        unique_count = len(freq)
        for freq, count in freq_count.items():
            total_removal = freq * count
            if k >= total_removal:
                k -= total_removal
                unique_count -= count
            else:
                unique_count -= k // freq
                break

        return unique_count