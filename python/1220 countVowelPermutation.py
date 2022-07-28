class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
            #dp
        """
        @cache
        def dp(i,p):
            if i == n:
                return 1
            ans = 0
            if p == "a":
                ans += dp(i+1,"e")
            elif p == "e":
                ans += dp(i+1,"a") + dp(i+1,"i")
            elif p == "i":
                ans += dp(i+1,"a") + dp(i+1,"e") + dp(i+1,"o") + dp(i+1,"u")
            elif p == "o":
                ans += dp(i+1,"i") + dp(i+1,"u")
            elif p == "u":
                ans += dp(i+1,"a")
                
        return (dp(1,"a") + dp(1,"e") + dp(1,"i") + dp(1,"o") + dp(1,"u")) % (10**9+7)

    def countVowelPermutation(self, n: int) -> int:
        a_count = e_count = i_count = o_count = u_count = 1
        MOD = 10 ** 9 + 7

        for i in range(1, n):
            a_count,e_count,i_count,o_count,u_count = (e_count + i_count + u_count) % MOD,\
             (a_count + i_count) % MOD,\
             (e_count + o_count) % MOD,\
             (i_count) % MOD,\
             (i_count + o_count) % MOD

        return (a_count + e_count + i_count + o_count + u_count) % MOD