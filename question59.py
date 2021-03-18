class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strdir = {}
        for word in strs:
            sortword = " ".join(sorted(word))
            if sortword in strdir:
                strdir[sortword].append(word)
            else:
                strdir[sortword] = [word]

        anagrams = []
        for item in strdir.values():
            anagrams.append(item)
        return anagrams

