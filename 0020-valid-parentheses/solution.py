class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
            # Map each opener to its matching closer
        opener_to_closer = {'(': ')', '{': '}', '[': ']'}

        for i in s:
                if i in opener_to_closer:
                    # Opening bracket → push its matching closing bracket
                    self.stack.append(opener_to_closer[i])
                else:
                    # Closing bracket → must match top of stack
                    if not self.stack or self.stack.pop() != i:
                        return False

            # At the end, no expected closers should be left
        return not self.stack

