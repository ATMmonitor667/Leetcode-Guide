from collections import defaultdict, deque
import heapq

class Twitter(object):

    def __init__(self):
        # Global timer to timestamp every tweet
        self.timer = 0
        
        # Map: userId -> List of [timestamp, tweetId]
        # We use a deque to easily append new tweets
        self.tweets = defaultdict(deque)
        
        # Map: userId -> Set of followeeIds
        # A Set is better than a List because it prevents duplicate follows
        self.followees = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # 1. Update global timer (decrement to use Min-Heap as Max-Heap later)
        self.timer -= 1
        
        # 2. Store the tweet with the time
        self.tweets[userId].appendleft((self.timer, tweetId))
        
        # Optimization: We only ever need the top 10. 
        # If a user has 1000 tweets, we can drop the old ones to save memory.
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        # 1. Start with the user's own tweets
        tweets_to_merge = []
        if self.tweets[userId]:
            tweets_to_merge.append(self.tweets[userId])
            
        # 2. Add tweets from everyone they follow
        for followeeId in self.followees[userId]:
            if self.tweets[followeeId]:
                tweets_to_merge.append(self.tweets[followeeId])
        
        # 3. Merge multiple sorted lists (The "Heap" approach)
        # heapq.merge is perfect for combining sorted iterators efficiently
        feed = heapq.merge(*tweets_to_merge)
        
        # 4. Take the top 10. 
        # Since we stored negative time, the "smallest" number is the most recent.
        result = []
        count = 0
        for time, tweetId in feed:
            result.append(tweetId)
            count += 1
            if count == 10:
                break
                
        return result

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # A user cannot follow themselves
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # discard() is safer than remove() because it won't crash if the key doesn't exist
        self.followees[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)