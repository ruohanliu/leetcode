class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
            #tree #serialization #preorder

            each node has has 1 indegree and 2 outdegree
            # node has 1 indegree 0 outdegree
        """

        #pretend root has 1 indegree
        total_degree = 1        
        for c in preorder.split(","):

            total_degree -= 1
            if total_degree < 0:
                return False
            if c != "#":
                total_degree += 2

        return total_degree == 0
