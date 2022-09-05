class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
            #simulation
        """
        stack = []
        pathLen = 0
        n = len(input)
        i = 0
        level = 0
        ans = 0
        while i < n:
            if input[i] == "\n":
                level = 0
                i+=1
            elif input[i] == "\t":
                level += 1
                i+=1
            else:
                while level < len(stack):
                    pathLen -= len(stack.pop())
                j = i
                while j < n and input[j] not in ("\n","\t"):
                    j += 1
                curr = input[i:j]
                if curr.find(".") > 0:
                    ans = max(ans,pathLen + len(stack) + len(curr))
                else:
                    stack.append(curr)
                    pathLen += len(curr)
                i = j
        return ans
