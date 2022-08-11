class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        """
            #greedy #dp #slidingwindow #important #hard #relation

            The boxes need to be delivered in the order they are given
        """
        n = len(boxes)
        # 1-indexed
        dp = [0]*(n+1)
        # min trips per delivery is 2
        trips = 2
        i = 0
        for j in range(n):
            # load
            maxWeight -= boxes[j][1]
            # different ports between curr and prev
            if j and boxes[j-1][0] != boxes[j][0]: trips += 1
            
            # unload if exceed limit or when cost till previous box is the same as till current box
            while (maxBoxes < j - i + 1 or maxWeight < 0) or (i < j and dp[i] == dp[i+1]):
                maxWeight += boxes[i][1]
                if boxes[i][0] != boxes[i+1][0]: trips-=1
                i += 1
            dp[j+1] = dp[i] + trips
        return dp[-1]