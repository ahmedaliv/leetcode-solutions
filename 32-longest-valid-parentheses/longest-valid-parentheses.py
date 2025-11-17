class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Short solution using the "parent index" idea.
        #
        # We push the index of every '(' onto the stack.
        # Each index represents the start of a new valid parent expression.
        #
        # Initialize the stack with -1, acting as the parent for the whole string.
        # This helps compute lengths when the valid substring starts at index 0.
        best = 0
        stk = [-1]

        for i, c in enumerate(s):
            if c == '(':
                # New opened sub-expression → push its index.
                stk.append(i)
            else:
                # ')' → close a sub-expression.
                # Pop the direct matching '(' index (or attempt to).
                stk.pop()

                if not stk:
                    # No parent exists → invalid ')'.
                    # Start a new parent boundary from this index.
                    stk.append(i)
                else:
                    # Valid match with a parent expression.
                    # Compute the length of the current valid substring:
                    # current_position - parent_start_index
                    best = max(best, i - stk[-1])

        return best
