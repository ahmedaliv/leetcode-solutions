from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(line_words: List[str], line_len: int) -> str:
            if len(line_words) == 1:
                return line_words[0] + ' ' * (maxWidth - line_len)

            total_spaces = maxWidth - line_len
            gaps = len(line_words) - 1
            space_per_gap = total_spaces // gaps
            extra = total_spaces % gaps

            line = []
            for i, w in enumerate(line_words[:-1]):
                line.append(w)
                spaces = space_per_gap + (1 if i < extra else 0)
                line.append(' ' * spaces)
            line.append(line_words[-1])

            return ''.join(line)

        def left_justify(line_words: List[str]) -> str:
            # Left-justify the last line
            line = ' '.join(line_words)
            return line + ' ' * (maxWidth - len(line))

        result = []
        line_words = []
        line_len = 0 

        for w in words:
            if line_len + len(line_words) + len(w) <= maxWidth:
                line_words.append(w)
                line_len += len(w)
            else:
                result.append(justify(line_words, line_len))
                line_words = [w]
                line_len = len(w)

        if line_words:
            result.append(left_justify(line_words))

        return result
