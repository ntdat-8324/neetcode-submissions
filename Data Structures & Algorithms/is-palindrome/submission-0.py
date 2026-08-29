class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        l = len(s)-1

        while f < l:

            if not self.alphaNum(s[f]):
                f += 1
                continue
            
            if not self.alphaNum(s[l]):
                l -= 1
                continue

            if s[f].lower() != s[l].lower():
                return False

            l -= 1
            f += 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

            

            
            