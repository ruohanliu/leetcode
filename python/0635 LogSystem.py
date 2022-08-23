class LogSystem:
    """
        #design #reduce #sorteddict
    """
    graIdx = {"Year":0,"Month":1,"Day":2,"Hour":3,"Minute":4,"Second":5}
    def __init__(self):
        from sortedcontainers import SortedDict
        self.log = SortedDict()
        

    def put(self, id: int, timestamp: str) -> None:
        if timestamp not in self.log:
            self.log[timestamp] = [id]
        else:
            self.lop[timestamp] += id,

    def _toStr(self,num):
        if num < 10:
            return f"0{num}"
        else:
            return str(num)

    def _truncate_timestamp(self,timestamp,granularity,start):
        parsed  = list(map(int,timestamp.split(":")))
        for i in range(6):
            if i <= self.graIdx[granularity]:
                continue
            parsed[i] = 0 if start else 99
        
        return ":".join(map(self._toStr,parsed))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start = self._truncate_timestamp(start,granularity,True)
        end = self._truncate_timestamp(end,granularity,False)
        i = self.log.bisect_left(start)
        j = self.log.bisect_right(end)
        return reduce(add,[self.log[ts] for ts in self.log.islice(i,j)],[])


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)