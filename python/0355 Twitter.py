class Twitter:
    """
        #heap #design
    """

    def __init__(self):
        self.g = defaultdict(set)
        self.tweet = defaultdict(deque)
        self.uuid = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].appendleft((self.uuid,tweetId))
        self.uuid -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = heapq.merge(*(self.tweet[user] for user in self.g[userId] | {userId}))
        return [tweet for _, tweet in itertools.islice(tweets, 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.g[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.g[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)