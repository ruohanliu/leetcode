class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        """
            #dp #precompute
        """
        @cache
        def dp(lap):
            if lap == 0:
                return -changeTime
            return min(lapRecord[i]+changeTime+dp(lap-i) for i in range(1,min(lap,maxLap)+1))

        # calculate best tire for each # of laps
        lapRecord = defaultdict(int)
        maxLap = 0
        for f,r in tires:
            lap = 1
            time = f
            lapTime = f
            while lap <= numLaps and lapTime < f+changeTime:
                maxLap = max(maxLap,lap)
                if lapRecord[lap] == 0 or time < lapRecord[lap]:
                    lapRecord[lap] = time
                lap+=1
                lapTime *= r
                time += lapTime

        return dp(numLaps)