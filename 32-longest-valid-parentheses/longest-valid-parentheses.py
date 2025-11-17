class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # This solution uses a stack of indices.
        # The stack always stores the *boundary* of the last unmatched position.
        #
        # stk = [-1] means:
        #   "Before the string starts, the last invalid position is at index -1"
        #
        # Whenever we find a valid pair, we measure the length from the current index
        # back to the last unmatched boundary.

        best = 0
        stk = [-1]   # Initial boundary before the string starts

        for i, c in enumerate(s):
            if c == '(':
                # Push index of '(' so that if it matches later,
                # we know the start position of this open parenthesis
                stk.append(i)
            else:
                # We found ')', remove one '(' index (attempt match)
                stk.pop()

                if not stk:
                    # No available '(' to match with → this ')' is invalid
                    # Set a new boundary at this index
                    stk.append(i)
                else:
                    # Valid pair found → compute the valid substring length.
                    # s[ stk[-1] + 1 : i ] is a valid range.
                    best = max(best, i - stk[-1])

        return best
