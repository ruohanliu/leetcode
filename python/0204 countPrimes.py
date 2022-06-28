class Solution:
    def countPrimes(self, n: int) -> int:
        """
            #prime
            Sieve of Eratosthenes
        """
        isPrime = [1] * n
        cnt = 0
        for num in range(2,n):
            if isPrime[num] == 1:
                cnt += 1
                for i in range(num**2,n,num):
                    isPrime[i] = 0

        return cnt
        