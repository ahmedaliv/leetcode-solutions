class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # We keep a stack of integers.
        # Each entry represents the length of a "segment" (a valid parentheses substring)
        # that is waiting to be attached to its parent segment.
        #
        # Example:
        # For "(())", we build inner segments first (2), then attach to the outer segment.
        
        stk = [0]   # Root segment (represents no substring before we start)
        best = 0
        opened = 0  # Tracks the number of unmatched "(" we have seen
        
        for i, c in enumerate(s):
            if c == '(':
                opened += 1
                
                # Start a new child segment.
                # Push a 0-length segment placeholder to accumulate future matches.
                stk.append(0)
            
            else:  # c == ')'
                if opened:
                    # We have a matching "(" available.
                    # Complete the child segment: add 2 characters for the matching pair.
                    child_len = stk[-1] + 2
                    stk.pop()  # Remove the child segment
                    
                    # Attach this completed child segment to its parent.
                    parent_len = stk[-1] + child_len
                    stk.pop()
                    
                    # Push the updated parent segment back.
                    stk.append(parent_len)
                    
                    opened -= 1
                    
                    # Track maximum valid substring length seen so far.
                    best = max(best, parent_len)
                
                else:
                    # Unmatched ')', so we reset segment.
                    # Start a new independent segment of length 0.
                    stk.append(0)
                    opened = 0
        
        return best
