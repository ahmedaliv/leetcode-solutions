from collections import defaultdict

class AllOne:
    def __init__(self):
        # string -> freq
        self.string_freq = defaultdict(int)
        # freq -> all strings with it
        self.freq_st = defaultdict(set)

    def inc(self, key: str) -> None:
        current_freq = self.string_freq[key]
        self.string_freq[key] = current_freq + 1

        if current_freq > 0:
            self.freq_st[current_freq].remove(key)
            if not self.freq_st[current_freq]:
                del self.freq_st[current_freq]
        
        self.freq_st[current_freq + 1].add(key)

    def dec(self, key: str) -> None:
        if key in self.string_freq:
            current_freq = self.string_freq[key]
            self.freq_st[current_freq].remove(key)
            if not self.freq_st[current_freq]:
                del self.freq_st[current_freq]

            if current_freq > 1:
                self.string_freq[key] = current_freq - 1
                self.freq_st[current_freq - 1].add(key)
            else:
                del self.string_freq[key]

    def getMaxKey(self) -> str:
        if not self.freq_st:
            return ""
        return next(iter(self.freq_st[max(self.freq_st)]))

    def getMinKey(self) -> str:
        if not self.freq_st:
            return ""
        return next(iter(self.freq_st[min(self.freq_st)]))
