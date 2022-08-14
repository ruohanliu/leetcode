class AuthenticationManager:
    """
        #ordereddict #design
    """
    def __init__(self, timeToLive: int):
        self.limit = timeToLive
        self.manager = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.clean(currentTime)
        self.manager[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.clean(currentTime)
        if tokenId in self.manager:
            self.manager[tokenId] = currentTime
            self.manager.move_to_end(tokenId,last=True)
        
    def clean(self,currentTime: int) -> None:
        while self.manager and next(iter(self.manager.values())) + self.limit <= currentTime:
            self.manager.popitem(last=False)
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.clean(currentTime)
        return len(self.manager)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)