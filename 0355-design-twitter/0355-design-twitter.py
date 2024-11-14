class User(object):
    def __init__(self):
        self.userId=0
        self.followee=set()
        self.newsfeed=[]#heap

class Twitter(object):

    def __init__(self):
        self.users=collections.defaultdict(User)#list of Users from user class
        self.postcnt=0
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.postcnt+=1 #no matter who is posting we always add to this count to maintain the order of the posts to later push to heap
        if userId not in self.users:
            user=User()
            user.userId=userId
            self.users[userId]=user

        user=self.users[userId]
        #max heap
        heapq.heappush(user.newsfeed, (-self.postcnt, tweetId))#remeber the tweetId is unique

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        user=self.users[userId]
        
        temp_heap=user.newsfeed[:]
        #add the news feed of the followee to the newsfeed of our userid user
        for followee in user.followee:
            for post in self.users[followee].newsfeed:
                heapq.heappush(temp_heap,post)
        
        #Retrieves the 10 most recent tweet IDs in the user's news feed
        post=[]
        for i in range(min(10,len(temp_heap))):
            post.append(heapq.heappop(temp_heap)[1])
        return post

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        follower=self.users[followerId]
        if followeeId not in self.users:
            followee=User()
            followee.userId=followeeId
            self.users[followeeId]=followee
        follower.followee.add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        follower=self.users[followerId]
        #remove followee from follower's followee list
        if followeeId in follower.followee:
            follower.followee.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)