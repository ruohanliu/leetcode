class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        """
            #dp #monostack #important #google
        """
        n = len(arr)
        # create nextHigher and nextLower array to store the index of the next higher/lower number for every number. Default to 0.
        nextHigher = [0] * n
        nextLower = [0] * n

        # sort by value and index. must sort twice
        monoStack = []
        for _,i in sorted([(x,i) for i,x in enumerate(arr)]):
            while monoStack and monoStack[-1] < i:
                nextHigher[monoStack.pop()] = i
            monoStack.append(i)

        monoStack = []
        for _,i in sorted([(-x,i) for i,x in enumerate(arr)]):
            while monoStack and monoStack[-1] < i:
                nextLower[monoStack.pop()] = i
            monoStack.append(i)
        
        #odd[i] indicates if at ith position, it can jump up
        odd = [0] * n
        even =[0] * n
        odd[-1] = 1
        even[-1] = 1
        for i in reversed(range(n-1)):
            odd[i] = even[nextHigher[i]]
            even[i] = odd[nextLower[i]]
        return sum(odd)
