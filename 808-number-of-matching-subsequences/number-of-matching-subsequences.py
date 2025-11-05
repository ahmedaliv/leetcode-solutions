from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        letter_to_indices = defaultdict(list)
        for i,w in enumerate(words):
            letter_to_indices[w[0]].append(i)
        pos = [0]*len(words)
        matched_words = 0
        for c in s:
            word_indices = letter_to_indices[c][:]
            letter_to_indices[c].clear()
            for w_i in word_indices:
                word = words[w_i]
                pos[w_i] +=1
                if pos[w_i] == len(word):
                    matched_words +=1
                else:
                    letter_to_indices[word[pos[w_i]]].append(w_i)
        return matched_words