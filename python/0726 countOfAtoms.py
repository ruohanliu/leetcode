class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
            #parse #important

            related: 394
        """
        c = Counter()
        m = [1]
        digit = '' 
        lower = ''
        
        for x in reversed(formula):
            element = x + lower
            if element.isdigit():
                digit = element + digit
            elif element.islower():
                lower = element
            elif element == ')':
                m.append(m[-1] * int(digit or 1))
                digit = ''
            elif element == '(':
                m.pop()
            else:
                c[element] += m[-1]*int(digit or 1)
                digit = ''
                lower = ''

        return "".join(str(k)+("" if v == 1 else str(v)) for k,v in sorted(c.items()))