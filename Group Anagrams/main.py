class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            sorted_word ="".join(sorted(word))
            if sorted_word in dictionary :
                dictionary[sorted_word].append(word)

            else :
                dictionary[sorted_word] = [word]

        return list(dictionary.values())            

    
        