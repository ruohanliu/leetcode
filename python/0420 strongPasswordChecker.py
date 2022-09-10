class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        """
            #greedy
        """
        n = len(password)
        cache = list(password)
        upper = 0
        lower = 0
        digit = 0
        for x in cache:
            if x.isupper():
                upper |= 1
            elif x.islower():
                lower |= 1
            elif x.isdigit():
                digit |= 1
        req = sum([upper,lower,digit])
        if n < 6:
            if n<5:
                return 6-n
            else:
                if req == 1:
                    return 2
                else:
                    return 1

        one = two = rep = 0
        
        i = 2
        while i < n:
            if cache[i-1] == cache[i-2] == cache[i]:
                sz = 3
                while i+1<n and cache[i] == cache[i+1]:
                    sz+=1
                    i+=1
                rep += sz//3
                if sz % 3 == 0:
                    one+=1
                elif sz %3 == 1:
                    two +=1
            i+=1
        if n <= 20:
            return max(rep,3-req)
        else:
            # For any repeating sequences with len % 3 == 0, we can reduce one replacement by deleting one character.
            # For any repeating sequences with len % 3 == 1, we can reduce one replacement by deleting two character. 
            # For the remaining sequences, we can reduce every replacement by deleting three character
            delete = n-20
            if delete >= one + 2*two:
                rep -= one + two + (delete-one-2*two)//3
            elif delete >= one:
                rep -= one + (delete-one)//2
            else:
                rep -= delete
            return delete + max(3-req,rep)