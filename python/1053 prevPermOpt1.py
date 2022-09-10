class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """
            #permutation
        """
        n = len(arr)
        # find rightside local maximum
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                mxIdx = i+1
                for j in range(i+1,n):
                    if arr[mxIdx]<arr[j]<arr[i]:
                        mxIdx = j
                arr[i],arr[mxIdx] = arr[mxIdx],arr[i]
                break
        return arr