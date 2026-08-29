class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []

        bracket_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        # [ [ { }]]

        for a in s:
            if a in bracket_dict:
                stack.append(bracket_dict[a])
            else:
                if len(stack) == 0:
                    return False

                if a == stack[-1]:
                    stack.pop()
                    continue

                else: return False
        if len(stack) == 0:
            return True
        return False
            

