class Solution:
    def decodeString(self, s: str) -> str:
        """
            #parse

            related 726

            O(n^2)
        """
        if not s:
            return ""
        ans = []
        bal = 0
        start= 0
        digit = []
        for i,c in enumerate(s):
            if bal == 0:
                if c.isalpha():
                    ans.append(c)
                elif c.isdigit():
                    digit.append(c)
                else:
                    bal += 1
                    start = i
            else:
                if c == "[":
                    bal += 1
                elif c == "]":
                    bal -= 1
                    if bal == 0:
                        ans.append(int("".join(digit)) * self.decodeString(s[start+1:i]))
                        digit = []
        return "".join(ans)
    
    def decodeString(self, s: str) -> str:
        stack = []
        cnt = 0
        curr = []
        for c in s:
            if c == '[':
                stack.append(curr)
                stack.append(cnt)
                curr = []
                cnt = 0
            elif c == ']':
                num = stack.pop()
                curr = stack.pop() + curr*num
            elif c.isdigit():
                cnt = cnt*10 + int(c)
            else:
                curr += c,
        return "".join(curr)