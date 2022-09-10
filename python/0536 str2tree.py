class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        """
            #parse
        """
        return eval(f"""TreeNode({s.replace("(", ", TreeNode(")})""") if s else None

    def str2tree(self, s: str) -> Optional[TreeNode]:
        num = ''
        stack = []
        for i in s:
            if i.isdigit() or i == '-': 
                num+=i
            elif i=='(': 
                if num: 
                    node = TreeNode(num)
                    num=''
                    stack.append(node)
            else:
                if num:
                    node = TreeNode(num)
                    num =''
                else:
                    node = stack.pop()
                if stack[-1].left==None:
                    stack[-1].left = node 
                else:
                    stack[-1].right = node 

        return stack[-1] if stack else TreeNode(num) if s else None