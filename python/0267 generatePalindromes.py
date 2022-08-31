class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        """
            #palindrome #permutation
        """
        c = Counter(s)
        perm = []
        cnt = 0
        center = ""
        for k in c:
            if c[k] % 2:
                cnt += 1
                if cnt > 1:
                    return []
                center = k
                perm.extend([k]*((c[k]-1)//2))
            else:
                perm.extend([k]*(c[k] // 2))
        ans = set()
        for left in itertools.permutations(perm):
            ans.add("".join(left)+center+"".join(reversed(left)))
        return ans