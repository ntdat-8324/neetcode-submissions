class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alb = [0]*26
        for c in s:
            alb[ord(c) - ord('a')] += 1
        for c in t:
            alb[ord(c) - ord('a')] -= 1
        for c in alb:
            if c != 0:
                return False
        return True