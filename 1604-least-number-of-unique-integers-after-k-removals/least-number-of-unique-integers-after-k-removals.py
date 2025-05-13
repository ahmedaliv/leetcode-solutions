class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        freq_values = sorted(freq.values())
        unique_count = len(freq)

        for v in freq_values:
            if v <= k:
                k-=v
                unique_count -= 1
            else:
                break
        return unique_count
