from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
            #re

            \ is the excape char

            ? quantifier matches pattern 0 or 1 time
            ? modifier odifies the *, +, ? or {M,N}'d regex that comes before to match as few times as possible.

            use r-string when there is \

            + needs escaping

            (?:...) is non-capturing group

            m = re.match(patter,str) returns a match object
            m.groups()[0] is same as m.group(1)

            re does not support capturing repeated group of the same patter

            test m before use
        """
        import re
        email_set = set()
        for email in emails:
            m = re.match("(.+?)(?:\+.*)?(@.+)",email)
            print(m.groups())
            email_set.add(m.group(1).replace(".","")+m.group(2))

        return len(email_set)
        
s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))