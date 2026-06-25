class Twitter:

    def  __init__(self):
        # id: [following...]
        self.follows = defaultdict(set)
        # id: [tweets...]
        self.tweets = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        tweets = self.tweets[userId]
        tweets.append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []

        # user's tweets
        all_tweets.extend(self.tweets[userId])

        # followees' tweets
        for followee in self.follows[userId]:
            if followee == userId:
                continue
            all_tweets.extend(self.tweets[followee])
        
        heapq.heapify(all_tweets)
        while len(all_tweets) > 10:
            heapq.heappop(all_tweets)
        
        all_tweets.sort(reverse=True)
        return [i for t, i in all_tweets]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

        
