from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []
        combinations = []
        combinations.append(("", 0, 0))  # Start with the empty combination

        while combinations:
            current, left, right = combinations.pop()  # Treat the list as a stack

            if left == n and right == n:
                result.append(current)
            if left < n:
                combinations.append((current + '(', left + 1, right))
            if right < left:
                combinations.append((current + ')', left, right + 1))

        return result