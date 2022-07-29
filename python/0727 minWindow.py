class Solution:
    def minWindow_tle(self, s1: str, s2: str) -> str:
        if len(s2) > len(s1):
            return ""
        m = len(s1)
        n = len(s2)

        indices = {}
        prev = [[]] * (n+1)
        curr = [[]] * (n+1)
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    curr[j+1] = prev[j]+[s1[i]]
                    if len(curr[j+1]) == n:
                        indices[i] = i
                else:
                    curr[j+1] = prev[j+1] if len(prev[j+1]) > len(curr[j]) else curr[j]
            prev,curr = curr,prev
        
        if indices:
            minLength = float("inf")
            ans = ""
            matched = list(s2)        
            for hi in indices:
                i = hi
                j = len(matched)-1
                invalid = False
                while not invalid and j>=0:
                    while not invalid and s1[i] != matched[j]:
                        i -= 1
                        if (hi-i) >= minLength:
                            invalid = True
                    j -= 1
                    i -= 1
                if (hi-i) < minLength:
                    minLength = hi-i
                    ans = s1[i+1:hi+1]
            return ans
        else:
            return ""

    def minWindow(self, s1: str, s2: str) -> str:
        """
            #dp #optimized #relation
        """
        if len(s2) > len(s1):
            return ""
        m = len(s1)
        n = len(s2)

        # curr[j] stores the starting index of substring in s1
        prev = [0] * (n+1)
        curr = [0] * (n+1)
        start = 0
        length = m + 1
        for i in range(m):
            prev[0] = i+1
            for j in range(n):
                if s1[i] == s2[j]:
                    curr[j+1] = prev[j]
                else:
                    curr[j+1] = prev[j+1]
            if curr[-1] and (i - curr[-1] + 2) < length:
                start = curr[-1] - 1
                length = i - curr[-1] + 2
            prev,curr = curr,prev
        
        return s1[start:start+length] if length < m+1 else ""