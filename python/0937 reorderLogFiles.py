from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for log in logs:
            if ord(log[-1]) < 65:
                digit.append(log)
            else:
                letter.append(log)
        letter.sort(key = lambda x : (x.split()[1:],x.split()[0]))
        return letter+digit

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
            #sort #customsort #lambda #split
        """
        def get_key(x):
            _id,rest = x.split(maxsplit = 1)
            return (0,rest,_id) if rest[0].isalpha() else (1,)

        return sorted(logs)
