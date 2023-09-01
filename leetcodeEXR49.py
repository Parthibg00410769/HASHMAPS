from collections import defaultdict
class solution:
    def Anagrams(self):
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        for value in anagram_map.values():
            result.append(value)

        return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = solution
print(s.Anagrams(strs))

