from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for str_ in strs:
            alb = [0] * 26
            for c in str_:
                alb[ord(c) - ord('a')] += 1
            d[tuple(alb)].append(str_)

        return list(d.values())



            
