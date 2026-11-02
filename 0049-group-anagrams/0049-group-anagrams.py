class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = dict()
        for i in strs:
            key = str(sorted(i))
            if key in dic:
                dic[key].append(i)
            else:
                dic[key] = [i] 
        return list(dic.values())