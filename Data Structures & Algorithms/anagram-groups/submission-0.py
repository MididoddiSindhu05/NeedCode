class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for words in strs:
            key = "".join(sorted(words))

            if key not in d:
                d[key] = []
            d[key].append(words)
        return list(d.values())