class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
            #palindrome #edgecase #important
            12321
            1221
            12345
            1000
            1001
            99
        """
        m = int(n)
        if m < 10 or (n[0] == "1" and int(n[1:]) == 0):
            return str(m - 1)
        elif m == 11 or (n[-1] == n[0] == "1" and int(n[1:-1]) == 0):
            return str(int(n) - 2)
        elif n[0] == "9" and n[0] * len(n) == n:
            return str(int(n) + 2)
        else:
            def build_palindrome(base: str, is_even_length = True) -> str:
                """
                Build a palindrome using the given base.
                
                e.g.
                build_palindrome("123", True) = "123321"
                build_palindrome("123", False) = "12321"
                """
                if is_even_length:
                    return base + ''.join(base[::-1])
                else:
                    return base + ''.join(base[:-1][::-1])
                
            is_n_even = len(n) % 2 == 0
            palindrome_base = int(n[0: len(n) // 2]) if is_n_even else int(n[0: len(n) // 2 + 1])

            is_n_palindrome = build_palindrome(str(palindrome_base), is_n_even) == n
            base_candidates = [palindrome_base - 1, palindrome_base + 1] if is_n_palindrome \
                else [palindrome_base - 1, palindrome_base, palindrome_base + 1]  # Maintains increasing order

            min_diff = float("inf")
            ans = None
            for base_candidate in base_candidates:
                candidate = int(build_palindrome(str(base_candidate), is_n_even))
                # print(f"candidate: {candidate} diff: {abs(candidate - int(n))}")
                if abs(candidate - m) < min_diff:
                    min_diff = abs(candidate - m)
                    ans = str(candidate)
            
            return ans
        