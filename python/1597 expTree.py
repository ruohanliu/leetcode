class Solution:
    """
        #design #parser #expressiontree #important

        standard expression parser implementation where parse-functions are called on those with the lowest precendence 
        and recursively invoke parse-functions of things with higher precendence

        operand is one digit number
    """
    def expTree(self, s: str) -> 'Node':
        tokens = collections.deque(s)
        return self.parse_expression(tokens)

    def parse_expression(self, tokens):
        l = self.parse_product(tokens)
        while tokens and tokens[0] in "+-":
            op = tokens.popleft()
            r = self.parse_product(tokens)
            l = Node(val=op, left=l, right=r)
        return l
    
    def parse_product(self, tokens):
        l = self.parse_parenthesis(tokens)
        while tokens and tokens[0] in "*/":
            op = tokens.popleft()
            r = self.parse_parenthesis(tokens)
            l = Node(val=op, left=l, right=r)
        return l

    def parse_parenthesis(self, tokens):
        if tokens[0] == '(':
            tokens.popleft() # consume '('
            node = self.parse_expression(tokens)
            tokens.popleft() # consume ')'
            return node
        else:
            return Node(val=tokens.popleft())