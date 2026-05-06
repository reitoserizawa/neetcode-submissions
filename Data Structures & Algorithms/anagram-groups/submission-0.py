class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            alph = [0] * 26
            for l in s:
                alph[ord(l)-ord('a')] += 1

            key = tuple(alph)
            res[key].append(s)
        
        return res.values()